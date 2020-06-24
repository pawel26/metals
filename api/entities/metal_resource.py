import datetime

from api.models import Metal


class MetalResource:
    def __init__(self, for_date, metal_code):
        self.for_date = for_date
        self.metal_code = metal_code
        self.metals = {'AU': 'gold', 'AG': 'silver'}

    def get_metal_based_on_date(self):
        if isinstance(self.for_date, str):
            import pdb; pdb.set_trace()
            return self.for_date.split('-')
        now = datetime.datetime.now()
        return now.year, now.month, now.day

    def get_instance(self):
        year, month, day = self.get_metal_based_on_date()
        metal, metal_created = Metal.objects.get_or_create(
            metal_name=self.metals[self.metal_code],
            datetime__year=year,
            datetime__month=month,
            datetime__day=day)
        import pdb;
        pdb.set_trace()
        if metal_created:
            metal.metal_name = self.metals[self.metal_code]
            metal.save()
        return metal
