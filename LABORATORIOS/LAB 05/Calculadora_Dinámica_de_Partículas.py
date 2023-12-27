import tkinter as tk
from tkinter import ttk
import math as math

class ParticleDynamicsCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora - Dinámica de Sistema de Partículas")

        self.masses = []
        self.velocities = {'x': [], 'y': [], 'z': []}
        self.positions = {'x': [], 'y': [], 'z': []}
        self.aceleracion = {'x': [], 'y': [], 'z': []}

        self.create_widgets()

    def create_widgets(self):
        # Entradas de datos
        self.mass_label = ttk.Label(self.root, text="DATOS DE PARTICULAS: ")
        self.mass_label.grid(row=0, column=2, padx=10, pady=10)

        self.mass_entry = ttk.Entry(self.root, width=15)
        self.mass_entry.insert(0, "0") 
        self.mass_entry.grid(row=5, column=2, padx=5, pady=5)
        self.mass_label = ttk.Label(self.root, text="Kg:")
        self.mass_label.grid(row=5, column=1, padx=5, pady=5)
        self.mass_label = ttk.Label(self.root, text="Masa:")
        self.mass_label.grid(row=5, column=0, padx=10, pady=10)

        self.mass_label = ttk.Label(self.root, text="Posición Inicial (x,y,z):")
        self.mass_label.grid(row=1, column=0, padx=10, pady=10)

        self.x_entry = ttk.Entry(self.root, width=15)
        self.x_entry.insert(0, "0") 
        self.x_entry.grid(row=1, column=2, padx=5, pady=5)
        self.x_label = ttk.Label(self.root, text="Px:")
        self.x_label.grid(row=1, column=1, padx=5, pady=5)

        self.y_entry = ttk.Entry(self.root, width=15)
        self.y_entry.insert(0, "0") 
        self.y_entry.grid(row=1, column=4, padx=5, pady=5)
        self.y_label = ttk.Label(self.root, text="Py:")
        self.y_label.grid(row=1, column=3, padx=5, pady=5)

        self.z_entry = ttk.Entry(self.root, width=15)
        self.z_entry.insert(0, "0") 
        self.z_entry.grid(row=1, column=6, padx=5, pady=5)
        self.z_label = ttk.Label(self.root, text="Pz:")
        self.z_label.grid(row=1, column=5, padx=5, pady=5)

        self.mass_label = ttk.Label(self.root, text="Velocidad Inicial (x,y,z):")
        self.mass_label.grid(row=2, column=0, padx=10, pady=10)

        self.vx_entry = ttk.Entry(self.root, width=15)
        self.vx_entry.insert(0, "0") 
        self.vx_entry.grid(row=2, column=2, padx=5, pady=5)
        self.vx_label = ttk.Label(self.root, text="Vx:")
        self.vx_label.grid(row=2, column=1, padx=5, pady=5)

        self.vy_entry = ttk.Entry(self.root, width=15)
        self.vy_entry.insert(0, "0") 
        self.vy_entry.grid(row=2, column=4, padx=5, pady=5)
        self.vy_label = ttk.Label(self.root, text="Vy:")
        self.vy_label.grid(row=2, column=3, padx=5, pady=5)

        self.vz_entry = ttk.Entry(self.root, width=15)
        self.vz_entry.insert(0, "0") 
        self.vz_entry.grid(row=2, column=6, padx=5, pady=5)
        self.vz_label = ttk.Label(self.root, text="Vz:")
        self.vz_label.grid(row=2, column=5, padx=5, pady=5)

        self.mass_label = ttk.Label(self.root, text="Aceleracion (x,y,z):")
        self.mass_label.grid(row=3, column=0, padx=10, pady=10)

        self.ax_entry = ttk.Entry(self.root, width=15)
        self.ax_entry.insert(0, "0") 
        self.ax_entry.grid(row=3, column=2, padx=5, pady=5)
        self.ax_label = ttk.Label(self.root, text="Ax:")
        self.ax_label.grid(row=3, column=1, padx=5, pady=5)

        self.ay_entry = ttk.Entry(self.root, width=15)
        self.ay_entry.insert(0, "0") 
        self.ay_entry.grid(row=3, column=4, padx=5, pady=5)
        self.ay_label = ttk.Label(self.root, text="Ay:")
        self.ay_label.grid(row=3, column=3, padx=5, pady=5)

        self.az_entry = ttk.Entry(self.root, width=15)
        self.az_entry.insert(0, "0") 
        self.az_entry.grid(row=3, column=6, padx=5, pady=5)
        self.az_label = ttk.Label(self.root, text="Az:")
        self.az_label.grid(row=3, column=5, padx=5, pady=5)

        # Resultados
        self.estado_label = ttk.Label(self.root, text="Estado:")
        self.estado_label.grid(row=6, column=0, padx=5, pady=10)
        self.entry_label = ttk.Label(self.root, text="Agregando...")
        self.entry_label.grid(row=6, column=1, padx=5, pady=10)
        self.note_label = ttk.Label(self.root, text="")
        self.note_label.grid(row=6, column=2, padx=5, pady=10)
        self.mass_label = ttk.Label(self.root, text="SOLUCIONES: ")
        self.mass_label.grid(row=7, column=2, padx=10, pady=10)

        # Botones de cálculo
        self.add_particle_button = ttk.Button(self.root, text="Agregar Partícula", command=self.add_particle)
        self.add_particle_button.grid(row=5, column=4, columnspan=2, pady=10)
        self.calcular_button = ttk.Button(self.root, text="CALCULAR", command=self.Calcular_Soluciones)
        self.calcular_button.grid(row=5, column=5, columnspan=2, pady=10)
        self.limpiar_button = ttk.Button(self.root, text="LIMPIAR", command=self.Limpiar)
        self.limpiar_button.grid(row=13, column=2, columnspan=2, pady=15)

        # Resultados

        self.Pos_Cmasa_label = ttk.Label(self.root, text="Posición del Centro de Masa  ->")
        self.Pos_Cmasa_label.grid(row=8, column=0, columnspan=2, pady=10)
        self.R_Pos_Cmasa_label = ttk.Label(self.root, text="\t\t\t\t\t", relief="groove")
        self.R_Pos_Cmasa_label.grid(row=8, column=2, columnspan=3, pady=10)
        
        self.Veloc_Cmasa_label = ttk.Label(self.root, text="Velocidad del Centro de Masa  ->")
        self.Veloc_Cmasa_label.grid(row=9, column=0, columnspan=2, pady=10)
        self.R_Veloc_Cmasa_label = ttk.Label(self.root, text="\t\t\t\t\t", relief="groove")
        self.R_Veloc_Cmasa_label.grid(row=9, column=2, columnspan=3, pady=10)

        self.MomentoL_Cmasa_label = ttk.Label(self.root, text="Momento Lineal del  ->\nCentro de Masa")
        self.MomentoL_Cmasa_label.grid(row=10, column=0, columnspan=2, pady=10)
        self.R_MomentoL_Cmasa_label = ttk.Label(self.root, text="\t\t\t\t\t", relief="groove")
        self.R_MomentoL_Cmasa_label.grid(row=10, column=2, columnspan=3, pady=10)

        self.Acele_Cmasa_label = ttk.Label(self.root, text="Aceleración  ->\ndel Centro de Masa")
        self.Acele_Cmasa_label.grid(row=11, column=0, columnspan=2, pady=10)
        self.R_Acele_Cmasa_label = ttk.Label(self.root, text="\t\t\t\t\t", relief="groove")
        self.R_Acele_Cmasa_label.grid(row=11, column=2, columnspan=3, pady=10)
        
        self.FuerzaT_Cmasa_label = ttk.Label(self.root, text="Fuerza Total del Centro de Masa  ->")
        self.FuerzaT_Cmasa_label.grid(row=12, column=0, columnspan=2, pady=10)
        self.R_FuerzaT_Cmasa_label = ttk.Label(self.root, text="\t\t\t\t\t", relief="groove")
        self.R_FuerzaT_Cmasa_label.grid(row=12, column=2, columnspan=3, pady=10)

    def add_particle(self):
        try:
            #Obteniendo los valores de los espacios.
            #Agregando loa valores a los arrays.
            self.masses.append(float(self.mass_entry.get()))
            self.positions['x'].append(float(self.x_entry.get()))
            self.positions['y'].append(float(self.y_entry.get()))
            self.positions['z'].append(float(self.z_entry.get()))
            self.velocities['x'].append(float(self.vx_entry.get()))
            self.velocities['y'].append(float(self.vy_entry.get()))
            self.velocities['z'].append(float(self.vz_entry.get()))
            self.aceleracion['x'].append(float(self.vx_entry.get()))
            self.aceleracion['y'].append(float(self.vy_entry.get()))
            self.aceleracion['z'].append(float(self.vz_entry.get()))
            
            mass = self.masses[-1]
            x = self.positions['x'][-1]
            y = self.positions['y'][-1]
            z = self.positions['z'][-1]
            vx = self.velocities['x'][-1]
            vy = self.velocities['y'][-1]
            vz = self.velocities['z'][-1]
            ax = self.aceleracion['x'][-1]
            ay = self.aceleracion['y'][-1]
            az = self.aceleracion['z'][-1]

            result = f" Partícula con Masa = {mass}\n Posición = ({x}, {y}, {z})\n Velocidad = ({vx}, {vy}, {vz})\n Aceleracion = ({ax}, {ay}, {az})"
            self.entry_label.config(text="AGREGADA  ->\nCORRECTAMENTE!",foreground="green")
            self.note_label.config(text=result,foreground="blue")

            #Vaciando los espacios de ingreso de datos.
            self.vaciar()

        except ValueError:
            self.entry_label.config(text="[Error]",foreground="red")

    def Calcular_Soluciones(self):
        self.entry_label.config(text="Completo",foreground="green")
        self.note_label.config(text="")

        total_mass = sum(self.masses)

        #   Posición del Centro de Masa
        x_cm = sum(m * x for m, x in zip(self.masses, self.positions['x'])) / total_mass
        y_cm = sum(m * y for m, y in zip(self.masses, self.positions['y'])) / total_mass
        z_cm = sum(m * z for m, z in zip(self.masses, self.positions['z'])) / total_mass
        mod = round(math.sqrt(x_cm**2 + y_cm**2 + z_cm**2),2)

        result = f"({round(x_cm,2)}, {round(y_cm,2)}, {round(z_cm,2)}) \t con Modulo \t=\t {mod} \tm"
        self.R_Pos_Cmasa_label.config(text=result,foreground="green")

        #   Velocidad del Centro de Masa
        vx_cm = sum(m * vx for m, vx in zip(self.masses, self.velocities['x']))
        vy_cm = sum(m * vy for m, vy in zip(self.masses, self.velocities['y']))
        vz_cm = sum(m * vz for m, vz in zip(self.masses, self.velocities['z']))
        mod = round(math.sqrt((vx_cm/total_mass)**2 + (vy_cm/total_mass)**2 + (vz_cm/total_mass)**2),2)

        result = f"({round(vx_cm/total_mass,2)}, {round(vy_cm/total_mass,2)}, {round(vz_cm/total_mass,2)}) \t con Modulo \t=\t {mod}\tm/s"
        self.R_Veloc_Cmasa_label.config(text=result,foreground="green")

        #   Momento Lineal del Centro de Masa
        mod = round(math.sqrt(vx_cm**2 + vy_cm**2 + vz_cm**2),2)

        result = f"({round(vx_cm,2)}, {round(vy_cm,2)}, {round(vz_cm,2)}) \t con Modulo \t=\t {mod}\tkg*m/s"
        self.R_MomentoL_Cmasa_label.config(text=result,foreground="green")

        #   Aceleracion del Centro de Masa
        ax_cm = sum(m * x for m, x in zip(self.masses, self.aceleracion['x']))
        ay_cm = sum(m * y for m, y in zip(self.masses, self.aceleracion['y']))
        az_cm = sum(m * z for m, z in zip(self.masses, self.aceleracion['z']))
        mod = round(math.sqrt((ax_cm/total_mass)**2 + (ay_cm/total_mass)**2 + (az_cm/total_mass)**2),2)

        result = f"({round(ax_cm/total_mass,2)}, {round(ay_cm/total_mass,2)}, {round(az_cm/total_mass,2)}) \t con Modulo \t=\t {mod} \tm/s^2"
        self.R_Acele_Cmasa_label.config(text=result,foreground="green")
        #vec = list((a*aa)+(b*bb)+(c*cc) for a,b,c,aa,bb,cc in zip(self.positions['x'],self.positions['y'],self.positions['z'],self.velocities['x'],self.velocities['y'],self.velocities['z']))
        #L = sum(m * v for m, v in zip(self.masses, vec)) / total_mass
        #result = f"con Modulo \t=\t {L}\tkg*m/s^2"
        #self.R_Acele_Cmasa_label.config(text=result,foreground="green")

        #   Fuerza Total del Centro de Masa
        mod = round(math.sqrt(ax_cm**2 + ay_cm**2 + az_cm**2),2)

        result = f"({round(ax_cm,2)}, {round(ay_cm,2)}, {round(az_cm,2)}) \t con Modulo \t=\t {mod} \tN"
        self.R_FuerzaT_Cmasa_label.config(text=result,foreground="green")

    def Limpiar(self):
        self.masses = []
        self.velocities = {'x': [], 'y': [], 'z': []}
        self.positions = {'x': [], 'y': [], 'z': []}
        self.aceleracion = {'x': [], 'y': [], 'z': []}

        #Vaciando los espacios de ingreso de datos.
        self.vaciar()
        self.note_label.config(text="")
        self.entry_label.config(text="Agregando...",foreground="black")
        self.R_Pos_Cmasa_label.config(text="\t\t\t\t\t")
        self.R_Veloc_Cmasa_label.config(text="\t\t\t\t\t")
        self.R_MomentoL_Cmasa_label.config(text="\t\t\t\t\t")
        self.R_Acele_Cmasa_label.config(text="\t\t\t\t\t")
        self.R_FuerzaT_Cmasa_label.config(text="\t\t\t\t\t")

    def vaciar(self):
        self.mass_entry.delete(0, tk.END)
        self.vx_entry.delete(0, tk.END)
        self.vy_entry.delete(0, tk.END)
        self.vz_entry.delete(0, tk.END)
        self.x_entry.delete(0, tk.END)
        self.y_entry.delete(0, tk.END)
        self.z_entry.delete(0, tk.END)
        self.ax_entry.delete(0, tk.END)
        self.ay_entry.delete(0, tk.END)
        self.az_entry.delete(0, tk.END)
        self.mass_entry.insert(0, "0")
        self.vx_entry.insert(0, "0")
        self.vy_entry.insert(0, "0")
        self.vz_entry.insert(0, "0")
        self.x_entry.insert(0, "0")
        self.y_entry.insert(0, "0")
        self.z_entry.insert(0, "0")
        self.ax_entry.insert(0, "0")
        self.ay_entry.insert(0, "0")
        self.az_entry.insert(0, "0")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("690x600")
    calculator = ParticleDynamicsCalculator(root)
    root.mainloop()
