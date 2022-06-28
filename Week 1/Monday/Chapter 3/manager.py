import uuid
import abc


class Sale (metaclass=abc.ABCMeta):
    """Abstract class for sales made by an IT company to a buyer."""
    @abc.abstractmethod
    def offer(self, buyer):
        pass

    @abc.abstractmethod
    def buy(self, answer):
        pass

    @classmethod
    def __subclasshook__(cls, c):
        if cls is Sale:
            attrs = set(dir(c))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented


class SalesManager:
    def __init__(self, buyer, SaleClass):
        self.sale = SaleClass()
        self.sale.buyer = buyer
        self.bought = 0
        self.declined = 0
        self.earned = 0

    def buy(self, answer):
        result = self.sale.buy(answer)
        if result > 0:
            self.bought += 1
            self.earned += result
        else:
            self.declined += 1

        return result

    def offer(self):
        return self.sale.offer()


class Manager:
    def __init__(self):
        self.services_offered = {}
        self.buyers_contacted = {}

    def register(self, service_offer):
        if not issubclass(service_offer, Sale):
            raise RuntimeError(
                "Your class does not have the right method"
            )
        id = uuid.uuid4()
        self.services_offered[id] = service_offer
        return id

    def give_offer(self, buyer, id):
        self.buyers_contacted[buyer] = SalesManager(
            buyer, self.services_offered[id]
        )

    def get_service(self, buyer):
        service = self.buyers_contacted[buyer]
        return service.offer()

    def check_response(self, buyer, answer):
        service = self.buyers_contacted[buyer]
        return service.buy(answer)

    def customer_summary(self, buyer):
        manager = self.buyers_contacted[buyer]
        return f"""
        {buyer}'s reaction to {manager.sale.__class__.__name__}:
        
        Times bought: {manager.bought}
        Times declined: {manager.declined}
        
        Money earned from buyer: ${manager.earned}
        """

