from manager import Sale

class ITService(Sale):
    def offer(self):
        return ("Good afternoon "
                + self.buyer
                + ". We want to offer you Cybersecurity services for $70.000."
                + " Do you accept?"
        )

    def buy(self, answer):
        if answer == "yes":
            return 70000
        else:
            return 0


class Project(Sale):
    def offer(self):
        return ("Good afternoon "
                + self.buyer
                + ". We want to offer your employees a 7-day course on IT for $3000."
                + " Do you accept?"
        )

    def buy(self, answer):
        if answer == "yes":
            return 3000
        else:
            return 0
