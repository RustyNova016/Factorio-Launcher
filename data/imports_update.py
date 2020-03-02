from data.imports import *
from data.data_file import *
from data.small_functions import *


def askreset(aaa):
    def butreset(aaa):
        aaa.reset()
        mai.destroy()
    mai = tk.tk()
    lab = tk.label(mai, text="data file broken. reset it?")
    lab.grid(row=0,column=0)
    reset_button = tk.button(mai, text="reset", command=lambda i=aaa: butreset(i))
    reset_button.grid(row=1,column=0)
    mai.mainloop()


settings = data_file(SETTINGS_PATH, SETTINGS_DICT)
factorio_configs = data_file(FACTORIO_CONFIG_PATH, FACTORIO_CONFIG_DICT)

if type(settings.loaded_file) is str:
    if settings.loaded_file == "cannot read file":
        askreset(settings)

if type(factorio_configs.loaded_file) is str:
    if factorio_configs.loaded_file == "cannot read file":
        askreset(factorio_configs)

if settings.loaded_file["version"] < SETTINGS_DICT["version"]:
    print("Updating data files")
    settings.loaded_file["version"] = SETTINGS_DICT["version"]
    settings.updatekeys()
    settings.write()
    factorio_configs.updatekeys()
    print("Data files successfully updated")


