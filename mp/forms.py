from django import forms
from django.forms import DateInput

from .models import repair_record, board_type, board_faults_categories, repair_record_progress, board


class BoardTypeForm(forms.ModelForm):
    class Meta:
        model = board_type
        fields = ('name',)


class RepairRecordForm(forms.ModelForm):
    suspect_fault_after_checkup = forms.ModelMultipleChoiceField(
        queryset=board_faults_categories.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = repair_record
        widgets = {
            'open_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'closed_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
      

        fields = ('board_serial_number', 'open_date', 'closed_date', 'issue_no', 'fault_local_agent',
                  'suspect_fault_after_checkup')
        

    def __init__(self, *args, **kwargs):
        super(RepairRecordForm, self).__init__(*args, **kwargs)
        self.fields['open_date'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['closed_date'].input_formats = ('%Y-%m-%dT%H:%M',)


class BoardFaultsCategoriesForm(forms.ModelForm):
    class Meta:
        model = board_faults_categories
        fields = ('board_type', 'board_issue')


class BoardForm(forms.ModelForm):
    
    status_choices = (
        ('Pass', 'Pass'),
        ('Unfixable', 'Unfixable'),
        ('In Progress', 'In Progress'),
        )
    status= forms.CharField(label='status', widget=forms.RadioSelect(choices=status_choices))
    class Meta:
        model = board
        fields = ('board_type', 'mac_no', 'batch_no', 'serial_number', 'status')



class RepairRecordProgressForm(forms.ModelForm):
    class Meta:
        model = repair_record_progress
        widgets = {
            'date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        
        }
        fields = ('repair_record', 'date', 'staff', 'workdone')
    
    def __init__(self, *args, **kwargs):
        super(RepairRecordProgressForm, self).__init__(*args, **kwargs)
        self.fields['date'].input_formats = ('%Y-%m-%dT%H:%M',)
