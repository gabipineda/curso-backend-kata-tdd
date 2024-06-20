je de programación como JavaScript. Aquí te muestro cómo podría lucir una posible implementación en JavaScript para cumplir con los requisitos que mencionaste:

class Greeter {
    greet(name) {
        let now = new Date();
        let hour = now.getHours();
        let trimmedName = name.trim();
        let capitalizedName = trimmedName.charAt(0).toUpperCase() + trimmedName.slice(1);

        if (hour >= 6 && hour < 12) {
            console.log(`Good morning ${capitalizedName}`);
            return `Hola ${capitalizedName}`;
        } else if (hour >= 18 && hour < 22) {
            console.log(`Good evening ${capitalizedName}`);
            return `Hola ${capitalizedName}`;
        } else {
            console.log(`Good night ${capitalizedName}`);
            return `Hola ${capitalizedName}`;
        }
    }
}

const greeter = new Greeter();
console.log(greeter.greet("   maría   "));
