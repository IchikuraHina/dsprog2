import flet as ft

#ボタンの一般的な特徴を設定し、ボタンがクリックされたときに実行されるコールバック関数 button_clicked を設定します。
class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        self.on_click = button_clicked
        self.data = text

#DigitButton クラスは CalcButton を継承しており、数字ボタンの外観（背景色と文字色）を設定
class DigitButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text, button_clicked, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE

#ActionButton クラスは CalcButton を継承しており、演算子ボタンの外観を設定
class ActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE

#ExtraActionButton クラスは、その他の機能（例えば、ACや +/- ボタン）のためのボタンを定義
class ExtraActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK

# CalculatorApp クラスは、電卓アプリのユーザーインターフェース全体を作成し、ボタンのレイアウトを定義
class CalculatorApp(ft.Container):
    # application's root control (i.e. "view") containing all other controls
    def __init__(self):
        super().__init__()
        self.reset()

        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=20)
        self.width = 500  # 幅を拡張
        self.bgcolor = ft.colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.result], alignment="end"),
                
                ft.Row(
                    controls=[
                        DigitButton(
                            text="X^2", button_clicked=self.button_clicked # 新しいボタン
                        ),
                        ExtraActionButton(
                            text="AC", button_clicked=self.button_clicked
                        ),
                        ExtraActionButton(
                            text="+/-", button_clicked=self.button_clicked
                        ),
                        ExtraActionButton(text="%", button_clicked=self.button_clicked),
                        ActionButton(text="/", button_clicked=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(
                            text="X^3", button_clicked=self.button_clicked # 追加
                        ),
                        DigitButton(text="7", button_clicked=self.button_clicked),
                        DigitButton(text="8", button_clicked=self.button_clicked),
                        DigitButton(text="9", button_clicked=self.button_clicked),
                        ActionButton(text="*", button_clicked=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(
                            text="10^X", button_clicked=self.button_clicked # 追加
                        ),
                        DigitButton(text="4", button_clicked=self.button_clicked),
                        DigitButton(text="5", button_clicked=self.button_clicked),
                        DigitButton(text="6", button_clicked=self.button_clicked),
                        ActionButton(text="-", button_clicked=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(
                            text="1/X", button_clicked=self.button_clicked # 追加
                        ),
                        DigitButton(text="1", button_clicked=self.button_clicked),
                        DigitButton(text="2", button_clicked=self.button_clicked),
                        DigitButton(text="3", button_clicked=self.button_clicked),
                        ActionButton(text="+", button_clicked=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(
                            text="π", button_clicked=self.button_clicked # 追加
                        ),
                        DigitButton(
                            text="0", expand=2, button_clicked=self.button_clicked
                        ),
                        DigitButton(text=".", button_clicked=self.button_clicked),
                        ActionButton(text="=", button_clicked=self.button_clicked),
                    ]
                ),
            ]
        )

    # button_clicked メソッドは、ボタンがクリックされたときに実行される関数です。この関数では、クリックされたボタンのデータに基づいて、表示を更新したり、計算を行ったりする。
    def button_clicked(self, e):
        data = e.control.data
        print(f"Button clicked with data = {data}")
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand == True:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data

        elif data in ("+", "-", "*", "/"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True

        elif data == "=":
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()

        elif data == "X^2":
            self.result.value = str(self.format_number(float(self.result.value) ** 2))
            self.reset()

        elif data == "X^3":
            self.result.value = str(self.format_number(float(self.result.value) ** 3))
            self.reset()

        elif data == "10^X":
            self.result.value = str(self.format_number(10 ** float(self.result.value)))
            self.reset()

        elif data == "1/X":
            if float(self.result.value) != 0:
                self.result.value = str(self.format_number(1 / float(self.result.value)))
            else:
                self.result.value = "Error"
            self.reset()

        elif data == "π":
            self.result.value = str(self.format_number(float(self.result.value) * 3.141592653589793))
            self.reset()

        elif data == "%":
            self.result.value = str(self.format_number(float(self.result.value) / 100))
            self.reset()

        elif data == "+/-":
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)
            elif float(self.result.value) < 0:
                self.result.value = str(self.format_number(abs(float(self.result.value))))

        self.update()

    # calculate メソッドは、2つのオペランドと演算子に基づいて計算を行います。このメソッドを用いることで、加算、減算、乗算、除算の結果を得ることができます。
    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    # calculate メソッドは、2つのオペランドと演算子に基づいて計算を行います。このメソッドを用いることで、加算、減算、乗算、除算の結果を得ることができる。
    def calculate(self, operand1, operand2, operator):
        if operator == "+":
            return self.format_number(operand1 + operand2)
        elif operator == "-":
            return self.format_number(operand1 - operand2)
        elif operator == "*":
            return self.format_number(operand1 * operand2)
        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True

# main 関数は、Fletアプリケーションを初期化し、ページに電卓アプリケーションを追加します。
def main(page: ft.Page):
    page.title = "Calc App"
    # create application instance
    calc = CalculatorApp()
    # add application's root control to the page
    page.add(calc)

# ft.app(target=main) でアプリケーションを実行します。
ft.app(target=main)