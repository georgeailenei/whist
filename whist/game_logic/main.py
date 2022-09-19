from interface.UI import UI
from services.controller import Controller
from domain.validate import ValidateCards


def main():
    card_validator = ValidateCards()
    controller = Controller(card_validator)
    interface = UI(controller)
    interface.run()


if __name__ == "__main__":
    main()
