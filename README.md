## ----EXPENSES API-----

# Como probar esta API:

La podemos probar desde Thunder Client, PostMan o desde el swagger.

1. Ingresar a la siguiente ruta: http://127.0.0.1:8000

2. Una vez ingresamos a la ruta podemos hacer las siguientes pruebas:
- Registrarnos con nuestro nombre de usuario y contraseña.
- Luego de registrarnos podemos logearnos ingresando nuestras credenciales de forma correcta.
- Podemos almacenar nuestros gastos.
- A los gastos tambien podemos filtrarlos de acuerdo si los hemos realizado en el ultimo mes, semana, etc.

## REGISTRO
3. Para registrarnos:
- Ingresar a la ruta: http://127.0.0.1:8000/users/register
- Dentro de esta ruta ingresar un nombre de usuario (username) y una contraseña (password).
- Si todo va bien veremos un mensaje que muestra tu usuario y tu contraseña hasheada.

## LOGIN
4. Para logearse:
- Ingresar a la ruta: http://127.0.0.1:8000/auth/login
- Dentro de esta ruta ingresar nuestro nombre de usuario (username) y contraseña (password).
- Si todo va bien veremos el token jwt. Copiarlo y guardarlo que nos servira para lo que viene

5. Para el CRUD de gastos:
- Ingresar el token jwt en Auth (dentro de Thunder Client)
- Luego ingresar a la ruta: http://127.0.0.1:8000/expenses.
- Elegir el metodo GET.
- Si el token es correcto veremos una lista de nuestras tareas. (la primera vez quizas este vacía).

## CREAR GASTO: 
- Ingresar a la ruta: http://127.0.0.1:8000/expenses/create_expense
- Elegir el metodo POST.
- Ingresar un JSON con el monto (amount), descripcion, y categoria de nuestro gasto. Ejemplo de JSON:

{
  "amount": 200,
  "description": "Limon",
  "category": "Frutas"
}

- Si todo va bien veremos a nuestro gasto creado.

## ACTUALIZAR GASTO:
- Ingresar a la ruta: http://127.0.0.1:8000/expenses/update_expense/{expense_id}
- Reemplazar {expense_id} por el id de tu gasto a actualizar. 
- Para saber cual es el id de tu gasto ingresar a: http://127.0.0.1:8000/expenses.
- Elegir el metodo PUT.
- Ingresar un JSON con el monto (amount), descripcion, y categoria de nuestro gasto. Ejemplo de JSON:

{
  "amount": 1000,
  "description": "Limones",
  "category": "Frutas"
}

- Si todo va bien veremos a nuestro gasto actualizado.

## ELIMINAR GASTO:
- Ingresar a la ruta: http://127.0.0.1:8000/expenses/delete_expense/{expense_id}.
- Reemplazar {expense_id} por el id de tu gasto a eliminar. 
- Para saber cual es el id de tu gasto ingresar a: http://127.0.0.1:8000/expenses.
- Elegir el metodo DELETE.
- Si todo salio bien, veremos un mensaje de que se elimino el gasto.