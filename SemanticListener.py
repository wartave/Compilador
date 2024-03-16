#semantic SemanticListener
import re
from ParserVictorListener import ParserVictorListener


class SemanticListener(ParserVictorListener):
    def __init__(self):
        self.variable_declaradas = set()
        self.errores = []
        self.funciones_declaradas = set()
        self.pila_contextos = [set()]
    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    def determinarTipo(self, expresion):
        # Expresión regular para buscar elementos de la expresión
        patron = r'("[^"]+"|\d+|\w+)'
        elementos = re.findall(patron, expresion)

        # Verificar el tipo de cada elemento
        for elemento in elementos:
            try:
                # Intentar convertir el elemento a entero
                int(elemento)
                return "NUMERO_ENTERO"
            except ValueError:
                pass

            try:
                # Intentar convertir el elemento a flotante
                float(elemento)
                return "NUMERO_FLOTANTE"
            except ValueError:
                pass
            if expresion.lower() == "true" or expresion.lower() == "false":
                return "BOOLEANO"    
            
            # Si no se pudo convertir a número, entonces es una cadena
            if elemento.startswith('"') and elemento.endswith('"'):
                return "CADENA"

        # Si no se puede determinar el tipo, retornar None
        return None
    
    def enterBloque(self, ctx):
        self.pila_contextos.append(set())

    def exitBloque(self, ctx):
        variables_bloque = self.pila_contextos.pop()
        self.variable_declaradas -= variables_bloque

    def enterPrograma(self, ctx):
        self.variable_declaradas.clear()
        self.funciones_declaradas.clear()
        self.pila_contextos = [set()]

    def enterDeclaracion_variable(self, ctx):
        identificador = ctx.IDENTIFICADOR().getText()
        tipo = ctx.expresion().getText()
        print(f"tipotipotipotipo semántico: El tipo '{tipo}' ya ha sido utilizado en este bloque.")
        if identificador in self.pila_contextos[-1]:
            self.errores.append(f"Error semántico: El nombre '{identificador}' ya ha sido utilizado en este bloque.")
            print(f"Error semántico: El nombre '{identificador}' ya ha sido utilizado en este bloque.")
        elif identificador in self.funciones_declaradas:
            self.errores.append(f"Error semántico: El nombre '{identificador}' ya ha sido utilizado en una funcion.")
            print(f"Error semántico: El nombre '{identificador}' ya ha sido utilizado en una funcion.")
        else:
            self.pila_contextos[-1].add(identificador)
            self.variable_declaradas.add(identificador)
            # Obtener la expresión asignada
            expresion_asignada = ctx.expresion().getText()

            # Determinar el tipo de la expresión
            tipo_expresion = self.determinarTipo(expresion_asignada)

            if tipo_expresion == "CADENA":
                # Dividir la expresión asignada en partes separadas por '+'
                partes_expresion = expresion_asignada.split("+")

                # Verificar si alguna parte después del primer '+' es un número entero
                for parte in partes_expresion[1:]:
                    parte = parte.strip()  # Eliminar espacios en blanco
                    if parte.isnumeric():
                        self.errores.append(f"Error semántico: No se puede concatenar una cadena con un número entero en la variable '{identificador}'.")
                        print(f"Error semántico: No se puede concatenar una cadena con un número entero en la variable '{identificador}'.")
                        break  # Terminar el bucle si se encuentra un número entero
            elif tipo_expresion in ["NUMERO_ENTERO", "NUMERO_FLOTANTE"]:
                # Dividir la expresión asignada en partes separadas por '+'
                partes_expresion = expresion_asignada.split("+")

                # Verificar si alguna parte después del primer '+' es una cadena
                for parte in partes_expresion[1:]:
                    parte = parte.strip()  # Eliminar espacios en blanco
                    if not (parte.isnumeric() or self.is_float(parte)):
                        self.errores.append(f"Error semántico: No se puede concatenar un número con una cadena en la variable '{identificador}'.")
                        print(f"Error semántico: No se puede concatenar un número con una cadena en la variable '{identificador}'.")
                        break  # Terminar el bucle si se encuentra una cadena
            else:
                print(f"El tipo de la variable '{identificador}' no se pudo determinar.")

    def exitExpresion_primaria(self, ctx):
        if ctx.IDENTIFICADOR():
            identificador = ctx.IDENTIFICADOR().getText()
            if identificador not in self.variable_declaradas:
                self.errores.append(f"Error semántico: La variable '{identificador}' no ha sido declarada previamente.")
                print(f"Error semántico: La variable '{identificador}' no ha sido declarada previamente.")

    def enterDeclaracion_funcion(self, ctx):
        self.pila_contextos.append(set())
        identificador = ctx.IDENTIFICADOR().getText()
        if identificador in self.variable_declaradas:
            self.errores.append(f"Error semántico: El nombre '{identificador}' ya ha sido utilizado como una variable.")
            print(f"Error semántico: El nombre '{identificador}' ya ha sido utilizado como una variable.")
        elif identificador in self.funciones_declaradas:
            self.errores.append(f"Error semántico: La función '{identificador}' ya ha sido declarada previamente.")
            print(f"Error semántico: La función '{identificador}' ya ha sido declarada previamente.")
        else:
            self.funciones_declaradas.add(identificador)

    def enterAsignacion(self, ctx):
        variable = ctx.IDENTIFICADOR().getText()
        if variable not in self.variable_declaradas:
            self.errores.append(f"Error semántico: enterAsignacion La variable '{variable}' no ha sido declarada previamente.")


    def exitDeclaracion_funcion(self, ctx):
        self.pila_contextos.pop()