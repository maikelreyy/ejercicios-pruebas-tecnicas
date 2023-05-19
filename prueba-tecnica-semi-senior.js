//crea una funcion que convierta un numero romano en un número decimal

function romanoAEntero(romano) {
    //crear un objeto con numeros romanos y sus correspondientes valores numéricos

    const numerosRomanos = {
        M: 1000,
        CM:900,
        D:500,
        C: 100,
        XC: 90,
        L: 50,
        XL: 40,
        X: 10,
        IX: 9,
        V: 5,
        IV: 4,
        II: 2,
        I: 1

    }

    //crear una variable para almacenar el resultado (inicializada en 0)
    let resultado = 0; 
    //recorrer numerosRomanos letra a letra
    for(let i = 0; i < romano.length; i++) {
    //console.log(romano[i], numerosRomanos[romano[i]]);

    //si la letra actual es la ultima o si el valor del siguiente caracter
    //es menor o igual al del actual, entonces añadimos el valor al resultado
        if (i === romano.length - 1 || numerosRomanos[romano[i + 1]] <= numerosRomanos[romano[i]]){
        resultado += numerosRomanos[romano[i]];
        } else {
    //si no, restar el valor de la letra actual al resultado
            resultado -= numerosRomanos[romano[i]];
    }
    //devolver el resultado
    return resultado;
}
}

console.log(romanoAEntero("XV"));