from data.imports_final import *

class main_menu():

    def create_config(self):
        loop = True

        def check_path(path):
            try:
                if os.path.exists(path):
                    try:
                        return ["Factorio version: " + get_factorio_version(path), 1]
                    except:
                        return ["No Factorio installation found"]
                else:
                    return ["The path doesn't exist"]
            except:
                return ["Invalid path"]


        def confirm():
            if check_path(path_entry.get())[1] == 1:
                global loop
                config_handlera = config_handler()
                config_handlera.create(name_entry.get(), path_entry.get())
                subwin.destroy()
                loop = False
        subwin = tk.Tk()

        title = tk.Label(subwin, text="Create a new factorio configuration")
        name_label = tk.Label(subwin, text="Name: ")
        path_label = tk.Label(subwin, text="Path of the installation: ")
        version_label = tk.Label(subwin, text="Factorio version: ")

        filesearch_button = tk.Button(subwin, text=">")
        ok_button = tk.Button(subwin, text="Create configuration", command=confirm)
        cancel_button = tk.Button(subwin, text="Cancel", command=subwin.destroy)

        name_entry = tk.Entry(subwin)
        path_entry = tk.Entry(subwin)

        title.grid(row=0, column=0, columnspan=2, sticky=tk.W, padx=2)
        name_label.grid(row=1, column=0, sticky=tk.W, padx=4)
        path_label.grid(row=2, column=0, sticky=tk.W, padx=4)
        version_label.grid(row=3, column=0, sticky=tk.W, padx=4)

        filesearch_button.grid(row=2, column=2, sticky=tk.E, padx=4)
        ok_button.grid(row=4, column=1, columnspan=2, sticky=tk.E)
        cancel_button.grid(row=4, column=0, sticky=tk.W, padx=4)

        name_entry.grid(row=1, column=1)
        path_entry.grid(row=2, column=1)

        while loop:
            version_label.configure(text=check_path(path_entry.get())[0])
            subwin.update()


    def datareset(self):
        settings.reset()
        factorio_configs.reset()

    def main_menu(self):
        main = tk.Tk()

        select_list = {}
        li = []
        for conf in factorio_configs.loaded_file["configs"]:
            select_list[conf["name"] + " (" + conf["version"] + ")"] = conf
            li.append(conf["name"] + " (" + conf["version"] + ")")

        vari = tk.StringVar(main)
        vari.set(li[0])

        configs_optionmenu = tk.OptionMenu(main, vari, *li)
        configs_optionmenu.grid(row=0, column=0)
        config_button = tk.Button(main, text="Config", command=self.create_config)
        config_button.grid(row=1, column=0)
        reset_button = tk.Button(main, text="Reset", command=self.datareset)
        reset_button.grid(row=2, column=0)
        launch_button = tk.Button(main, text="Launch Factorio", command=lambda: self.factorio_launch(select_list[vari.get()]["exe_path"]))
        launch_button.grid(row=3, column=0)

        main.mainloop()

    def factorio_launch(self, factorio_path):
        os.startfile(factorio_path)