from django.contrib import admin

from .models import board_type, repair_record, repair_record_progress, board_faults_categories, board

admin.site.site_header = 'MeshPower'  # default: "Django Administration"
admin.site.index_title = ''  # default: "Site administration"
admin.site.site_title = ''  # default: "Django site admin"

admin.site.register(board_type)


class boardFaultCategoriesAdmin(admin.ModelAdmin):
    list_display = ['board_type', 'board_issue']


admin.site.register(board_faults_categories, boardFaultCategoriesAdmin)


class boardAdmin(admin.ModelAdmin):
    list_display = ['board_type', 'mac_no', 'batch_no', 'serial_number', 'status']


admin.site.register(board, boardAdmin)


class repairRecordAdmin(admin.ModelAdmin):
    list_display = ['issue_no', 'open_date', 'closed_date', 'board_serial_number', 'get_board_issues']


admin.site.register(repair_record, repairRecordAdmin)


class repairRecordProgressAdmin(admin.ModelAdmin):
    list_display = ['repair_record', 'staff', 'workdone', 'date']


admin.site.register(repair_record_progress, repairRecordProgressAdmin)
