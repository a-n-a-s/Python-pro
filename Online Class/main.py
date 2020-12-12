# imports
import datetime
import jin

# collecting date in 'x'

x = datetime.datetime.now()

# specifying buttons accroding to period
first_period = '//html//body//app//div//mat-sidenav-container//mat-sidenav-content//edmx-parent-container//edmx-team-meeting//div//div//div//div[1]//div[2]//div//div//div//table//tbody//tr[1]//td[4]//button//span'

second_period = '//html//body//app//div//mat-sidenav-container//mat-sidenav-content//edmx-parent-container//edmx-team-meeting//div//div//div//div[1]//div[2]//div//div//div//table//tbody//tr[2]//td[4]//button//span'

third_period = '//html//body//app//div//mat-sidenav-container//mat-sidenav-content//edmx-parent-container//edmx-team-meeting//div//div//div//div[1]//div[2]//div//div//div//table//tbody//tr[3]//td[4]//button//span'

fourth_period = '//html//body//app//div//mat-sidenav-container//mat-sidenav-content//edmx-parent-container//edmx-team-meeting//div//div//div//div[1]//div[2]//div//div//div//table//tbody//tr[4]//td[4]//button//span'

fifth_period = '//html//body//app//div//mat-sidenav-container//mat-sidenav-content//edmx-parent-container//edmx-team-meeting//div//div//div//div[1]//div[2]//div//div//div//table//tbody//tr[5]//td[4]//button//span'


# getting hour and minutes

hour = x.hour
minute = x.minute

# if else accroding to time

if (hour == 8 and minute == 25):
    joinClass(first_period)
elif (hour == 9 and minute == 30):
    joinClass(second_period)
elif (hour == 10 and minute == 15):
    joinClass(third_period)
elif (hour == 11 and minute == 15):
    joinClass(fourth_period)
elif (hour == 12 and minute == 00):
    joinClass(fifth_period)
else:
    print("It is Not The Time For Online Classes")
    