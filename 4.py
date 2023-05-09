import datetime
import jdatetime

# خواندن تاریخ تولد کاربر با فرمت مورد نظر
birthday_str = input("Enter your birthdate (format: dd/mm/yyyy): ")
birthday = datetime.datetime.strptime(birthday_str, "%d/%m/%Y").date()

# محاسبه مجموع کل ثانیه‌های سپری شده از عمر کاربر
age_seconds = (datetime.date.today() - birthday).total_seconds()
print(f"You have lived {age_seconds:,} seconds so far.")

# محاسبه تعداد روزها و دقایق باقی‌مانده تا جشن تولد بعدی
next_birthday_year = datetime.date.today().year
if datetime.date.today() > datetime.date(next_birthday_year, birthday.month, birthday.day):
    next_birthday_year += 1
next_birthday = datetime.date(next_birthday_year, birthday.month, birthday.day)
time_to_next_birthday = next_birthday - datetime.date.today()
print(f"Your next birthday is in {time_to_next_birthday.days} days and {time_to_next_birthday.seconds//60} minutes.")

# تبدیل تاریخ تولد به تاریخ جلالی
birthday_jalali = jdatetime.date.fromgregorian(date=birthday)
print(f"Your birthday in Jalali calendar: {birthday_jalali.strftime('%Y/%m/%d')}")