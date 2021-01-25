from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.forms import inlineformset_factory
from .models import board,board_type,board_faults_categories,repair_record
from mp.forms import BoardTypeForm, BoardFaultsCategoriesForm, BoardForm, RepairRecordForm, RepairRecordProgressForm

@ login_required
def index(request):
   
    Board_Type=board_type.objects.all()
    counter={}
    for bt in Board_Type:
        tcounter=0
        BoardType=board_type.objects.get(board_type_id=bt.board_type_id)
        boards=board.objects.filter(board_type=BoardType)
        for b in boards:
            tcounter= tcounter+repair_record.objects.filter(board_serial_number=b).count()
        counter[bt]=tcounter
    context={'boardTypes':Board_Type,'boards':boards,'repairs':counter}
    return render(request, 'dashboard.html',context)

def faultCount(request,board_type_id):
    counter=0
    counter = counter+[b.repair_record_set.all.count for b in board_type_id.board_set.all]
    return render(request, 'dashboard.html',{'TotalFaults':counter})


def boardTypeResult(request):
    if request.method == 'POST':
        form = BoardTypeForm(request.POST)
        if form.is_valid():
            boardtype = form.save()
            return redirect('new_board',boardtype.board_type_id)
    else:
        form = BoardTypeForm()
    return render(request, 'board_type.html', {'form': form})

def boardresult(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save()
            return redirect('rrepair',board.serial_number)
    else:
        form = BoardForm()

    return render(request, 'board.html', {'form': form})


def board_fault(request,board_type_id):
    Board_Type=board_type.objects.get(board_type_id=board_type_id)
    init={'board_type':Board_Type}
    form = BoardFaultsCategoriesForm(initial=init)
    if request.method == 'POST':
        form = BoardFaultsCategoriesForm(request.POST)
        if form.is_valid():
            boarfault = form.save()
            return redirect('new_board',Board_Type.board_type_id)
    return render(request, 'board_fault.html', {'form': form})


def repair_record_progress(request,repair_record_id):
    repairRecord=repair_record.objects.get(repair_record_id=repair_record_id)
    form = RepairRecordProgressForm(initial={'repair_record':repairRecord})
    if request.method == 'POST':
        form = RepairRecordProgressForm(request.POST)
        if form.is_valid():
            boardrepairprogress = form.save()
            return redirect('home')
    # else:
    #     form = RepairRecordProgressForm()
    return render(request, 'repair_record.html', {'form': form})


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def searchBoard(request):
    serial_number=request.GET.get('serialNum')
    if (serial_number!=''):
        serial_with_accepted_length=serial_number[0:12]
        init={'board_serial_number':serial_with_accepted_length}
        try:
            oneBoard= board.objects.get(serial_number=serial_with_accepted_length)
            return render(request,'detail.html', {'boardDetail':oneBoard})
        except ObjectDoesNotExist:
            form = BoardForm(initial=init)
            return redirect('board')
    return redirect('home')

def detail(request,board_id):
    oneBoard= board.objects.get(board_id=board_id)
    return render(request,'detail.html', {'boardDetail':oneBoard})

def board_type_detail(request,board_type_id):
    counter=0
    totalFaultCounter=0
    Board_Type=board_type.objects.get(board_type_id=board_type_id) 
    boards=board.objects.filter(board_type=Board_Type)
    suspected_fault={}
    faultCounter=0
    sub_suspected_fault={}
    pre_Counting_array=[]
    for b in boards:  
        counter=counter + b.repair_record_set.all().count()
        for record in b.repair_record_set.all(): 
            totalFaultCounter=totalFaultCounter+record.suspect_fault_after_checkup.all().count()
            pre_Counting_array.append(list(record.suspect_fault_after_checkup.all()))
    
    for faults in pre_Counting_array:
        faultCounter=1
        percent=0
        for f in faults:
            if f in suspected_fault.keys():
                faultCounter=sub_suspected_fault[f]+1
            percent= Decimal((faultCounter*100)/totalFaultCounter)
            sub_suspected_fault[f]=faultCounter
            sub_suspected_fault['percent']=round(percent,2)
            suspected_fault[f]={'count':sub_suspected_fault[f],'percent':round(percent,2)}

    all_fault_record=board_faults_categories.objects.all().filter(board_type=Board_Type)
    context={'boardTypeDetail':Board_Type,"Total_Repair_Record":counter,'all_fault_record':all_fault_record,'suspected_faults':suspected_fault,'totalFaultCounter':totalFaultCounter}
    return render(request,'board_type_detail.html', context)




def repair_record_history(request,board_type_id):
    Board_Type=board_type.objects.get(board_type_id=board_type_id) 
    boards=board.objects.filter(board_type=Board_Type)
    context={'boards':boards}
    return render(request,'repair_record_history.html', context)

    


def update(request, board_id):
    oneBoard= board.objects.get(board_id=board_id)
    form = BoardForm(instance = oneBoard)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=oneBoard)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        return render(request, 'board.html', {'form': form})

def delete(request, board_id):
    oneBoard= board.objects.get(board_id=board_id)
    if request.method == 'POST':
        oneBoard.delete()
        return redirect('home')
    return render(request, 'delete_board.html', {'item':oneBoard}) 

def deleteType(request, board_type_id):
    Board_Type=board_type.objects.get(board_type_id=board_type_id)
    if request.method == 'POST':
        Board_Type.delete()
        return redirect('home')
    return render(request, 'delete_board_type.html', {'item':Board_Type})


def repair(request,serialNum):
    board_serial_number = board.objects.get(serial_number=serialNum)
    board_type=board_serial_number.board_type
    issues=board_faults_categories.objects.all().filter(board_type=board_type)
    init={'board_serial_number':board_serial_number}
    form = RepairRecordForm(initial=init)
    form.fields['suspect_fault_after_checkup'].queryset=issues
    if request.method == 'POST':
        form = RepairRecordForm(request.POST)
        if form.is_valid():
            boardrecord = form.save()
            return redirect('repair_record_progress',boardrecord.repair_record_id)
    return render(request, 'repair_record.html', {'form': form})


def getBoardTypefromSerial(request,board_id):
    board_serial_number = board.objects.get(board_id=board_id)
    board_type=board_serial_number.board_type
    return redirect('new_board',board_type.board_type_id)