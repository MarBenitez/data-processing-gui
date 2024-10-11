from view import View
from presenter import Presenter
from model import Model

def main() -> None:
    model = Model()
    view = View()
    presenter = Presenter(model, view)
    view.presenter = presenter
    presenter.run()

if __name__ == "__main__":
    main()

