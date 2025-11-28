import math
import sys
import json
import os

class EngineeringCalculator:
    def __init__(self):
        self.history = []
        self.load_history()
        self.constants = {
            'pi': math.pi,
            'e': math.e,
            'sqrt2': math.sqrt(2),
            'golden_ratio': (1 + math.sqrt(5)) / 2
        }
    
    def load_history(self):
        """Загружает историю вычислений из файла, если он существует"""
        if os.path.exists('calc_history.json'):
            try:
                with open('calc_history.json', 'r') as f:
                    self.history = json.load(f)
            except:
                self.history = []
    
    def save_history(self):
        """Сохраняет историю вычислений в файл"""
        with open('calc_history.json', 'w') as f:
            json.dump(self.history, f)
    
    def add_to_history(self, expression, result):
        """Добавляет вычисление в историю"""
        self.history.append({
            'expression': expression,
            'result': result,
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        if len(self.history) > 100:  # Ограничиваем историю 100 записями
            self.history = self.history[-100:]
        self.save_history()
    
    def show_history(self):
        """Показывает историю вычислений"""
        if not self.history:
            print("История пуста")
            return
        
        print("\n===== ИСТОРИЯ ВЫЧИСЛЕНИЙ =====")
        for i, item in enumerate(reversed(self.history[-10:]), 1):  # Показываем последние 10 записей
            print(f"{i}. {item['expression']} = {item['result']} ({item['timestamp']})")
        print("===========================\n")
    
    def clear_history(self):
        """Очищает историю вычислений"""
        self.history = []
        self.save_history()
        print("История очищена")
    
    def show_constants(self):
        """Показывает доступные константы"""
        print("\n===== ДОСТУПНЫЕ КОНСТАНТЫ =====")
        for name, value in self.constants.items():
            print(f"{name} = {value}")
        print("===========================\n")
    
    def calculate(self, expression):
        """Вычисляет математическое выражение"""
        try:
            # Заменяем константы на их значения
            for const_name, const_value in self.constants.items():
                expression = expression.replace(const_name, str(const_value))
            
            # Безопасное вычисление выражения
            result = eval(expression, {"__builtins__": None}, {
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'asin': math.asin,
                'acos': math.acos,
                'atan': math.atan,
                'sinh': math.sinh,
                'cosh': math.cosh,
                'tanh': math.tanh,
                'log': math.log,
                'log10': math.log10,
                'log2': math.log2,
                'sqrt': math.sqrt,
                'pow': math.pow,
                'exp': math.exp,
                'abs': abs,
                'round': round,
                'pi': math.pi,
                'e': math.e,
                'ceil': math.ceil,
                'floor': math.floor,
                'factorial': math.factorial,
                'degrees': math.degrees,
                'radians': math.radians
            })
            
            self.add_to_history(expression, result)
            return result
        except Exception as e:
            return f"Ошибка: {str(e)}"
    
    def run(self):
        """Запускает калькулятор"""
        print("===== ИНЖЕНЕРНЫЙ КАЛЬКУЛЯТОР =====")
        print("Доступные функции:")
        print("  - Тригонометрические: sin(x), cos(x), tan(x), asin(x), acos(x), atan(x)")
        print("  - Гиперболические: sinh(x), cosh(x), tanh(x)")
        print("  - Логарифмы: log(x, base), log10(x), log2(x)")
        print("  - Степени и корни: pow(x, y), sqrt(x), exp(x)")
        print("  - Константы: pi, e, sqrt2, golden_ratio")
        print("  - Другие функции: abs(x), round(x), ceil(x), floor(x), factorial(x)")
        print("  - Углы: radians(x), degrees(x)")
        print("\nКоманды:")
        print("  - history - показать историю вычислений")
        print("  - clear - очистить историю")
        print("  - constants - показать константы")
        print("  - exit - выход из программы")
        print("===========================\n")
        
        while True:
            try:
                user_input = input("Введите выражение: ").strip().lower()
                
                if user_input == 'exit':
                    print("Спасибо за использование калькулятора!")
                    break
                elif user_input == 'history':
                    self.show_history()
                    continue
                elif user_input == 'clear':
                    self.clear_history()
                    continue
                elif user_input == 'constants':
                    self.show_constants()
                    continue
                elif not user_input:
                    continue
                
                result = self.calculate(user_input)
                print(f"Результат: {result}\n")
                
            except KeyboardInterrupt:
                print("\nПрограмма прервана пользователем.")
                break
            except Exception as e:
                print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    import datetime
    calc = EngineeringCalculator()
    calc.run()