import jdatetime
import convert_numbers


class JalaliDateTime:

    @property
    def year_en(self):
        return str(jdatetime.date.today().year)

    @property
    def year_fa(self):
        return convert_numbers.english_to_persian(str(jdatetime.date.today().year))

    @property
    def month_en(self):
        return str(jdatetime.date.today().month)

    @property
    def month_fa(self):
        return convert_numbers.english_to_persian(str(jdatetime.date.today().month))

    @property
    def month_name_en(self):
        return jdatetime.date.today().jmonth()

    @property
    def month_name_fa(self):
        return jdatetime.date.today().j_months_fa[jdatetime.date.today().month - 1]

    @property
    def day_en(self):
        return str(jdatetime.date.today().day)

    @property
    def day_fa(self):
        return convert_numbers.english_to_persian(str(jdatetime.date.today().day))

    @property
    def date_en(self):
        return self.year_en + '/' + self.month_en + '/' + self.day_en

    @property
    def date_fa(self):
        return self.year_fa + '/' + self.month_fa + '/' + self.day_fa

    @property
    def hour_en(self):
        return str(jdatetime.datetime.now().time().hour)

    @property
    def hour_fa(self):
        return convert_numbers.english_to_persian(str(jdatetime.datetime.now().time().hour))

    @property
    def minute_en(self):
        return str(jdatetime.datetime.now().time().minute)

    @property
    def minute_fa(self):
        return convert_numbers.english_to_persian(str(jdatetime.datetime.now().time().minute))

    @property
    def second_en(self):
        return str(jdatetime.datetime.now().time().second)

    @property
    def second_fa(self):
        return convert_numbers.english_to_persian(str(jdatetime.datetime.now().time().second))

    @property
    def time_en(self):
        return self.hour_en + ':' + self.minute_en + ':' + self.second_en

    @property
    def time_fa(self):
        return self.hour_fa + ':' + self.minute_fa + ':' + self.second_fa





