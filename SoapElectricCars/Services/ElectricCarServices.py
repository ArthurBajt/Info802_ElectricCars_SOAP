from spyne import ServiceBase, rpc, Unicode, Iterable, AnyDict
from SoapElectricCars.Controller import ElectricCarsController


class ElectricCarServices(ServiceBase):
    @rpc(_returns=AnyDict)
    def get_all_cars(ctx):
        return ElectricCarsController.get_all_electric_cars()


    @rpc(_returns=Unicode)
    def generate_fake_cars(cls):
        ElectricCarsController.generate_fake_cars()
        return "Ok"
