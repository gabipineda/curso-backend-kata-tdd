class Greeter:
    def greet(self, name):
        import datetime
        
        now = datetime.datetime.now()
        hour = now.hour
        trimmed_name = name.strip()
        capitalized_name = trimmed_name.capitalize()
        
        if 6 <= hour < 12:
            print(f"Good morning {capitalized_name}")
            return f"Hola {capitalized_name}"
        elif 18 <= hour < 22:
            print(f"Good evening {capitalized_name}")
            return f"Hola {capitalized_name}"
        else:
            print(f"Good night {capitalized_name}")
            return f"Hola {capitalized_name}"

greeter = Greeter()
print(greeter.greet("   María   "))
