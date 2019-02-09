#!/usr/bin/python
import os
import string
import re
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox

FILES = {
	'select': None,
	'bib': None
}
FIGURE_URLS = ""

class Prompt:
	def __init__(self):
		self.root = Tk()

		global FILES
		self.gui_btns = {'':''}
		self.gui_vars = {'':''}

		main = Frame(self.root)
		main.pack( side = TOP,expand=1,fill='both' )
		self.gui_vars['select'] = StringVar()
		Button(main, text = 'Select File', width = 10, command=self.FileSelection).pack( side = RIGHT, padx=(5, 5), pady=(5, 5) )
		Entry(main, state = DISABLED, textvariable=self.gui_vars['select'], width = 50, relief = SUNKEN ).pack( side = LEFT, expand=1,fill=X, padx=(5, 5), pady=(5, 5))
		
		main = Frame(self.root)
		main.pack( side = TOP,expand=1,fill='both' )
		self.gui_vars['bib'] = StringVar()
		Button(main, text = 'Select .bib', width = 10, command=self.BibSelection).pack( side = RIGHT, padx=(5, 5), pady=(5, 5) )
		Entry(main, state = DISABLED, textvariable=self.gui_vars['bib'], width = 50, relief = SUNKEN ).pack( side = LEFT, expand=1,fill=X, padx=(5, 5), pady=(5, 5))

		main = Frame(self.root)
		main.pack( side = TOP )
		Button(main, text = "Run", width = 10, command=self.Run).pack(side=RIGHT)
		self.running = StringVar()
		self.running.set('Select Files')
		self.runningbtn = Entry(main, textvariable=self.running, width = 10, background='firebrick1')
		self.runningbtn.pack(side=RIGHT,expand=1,fill='both')

		editor = Frame(self.root, width=50)
		editor.pack( side = TOP,expand=1,fill='both' , pady=(10, 0) , padx=(5, 5))

		scrollbar = Scrollbar(editor)
		scrollbar.pack(side=RIGHT,fill=Y)
		self.editor = Text(editor, yscrollcommand=scrollbar.set, width = 50)
		self.editor.pack(side=LEFT,expand=1,fill='both')

		self.gui_btns['save'] = Button(self.root, text = 'Save', width = 10, command=self.FileSave)
		self.gui_btns['save'].pack( side = TOP, padx=(5, 5), pady=(5, 5) )

		self.root.mainloop()

	def callback(self):
		global FIGURE_URLS
		FIGURE_URLS = self.e.get().split(',')
		self.root.destroy()

	def BibSelection(self):
		global FILES
		FILES['bib'] = filedialog.askopenfilename(title = "Select BIB file",filetypes = (("BIB files","*.bib"),("all files","*.*")))
		if FILES['bib'] != None:
			self.gui_vars['bib'].set(FILES['bib'])
		else:
			self.gui_vars['bib'].set('')

	def FileSelection(self):
		global FILES
		FILES['select'] = filedialog.askopenfilename(title = "Select TeX file",filetypes = (("TeX files","*.tex"),("all files","*.*")))
		if FILES['select'] != None:
			self.gui_vars['select'].set(FILES['select'])
		else:
			self.gui_vars['select'].set('')

	def FileSave(self):
		global FILES
		FILES['save'] = filedialog.asksaveasfile(mode='w+', defaultextension=".html", filetypes = (("HTML files","*.html"),("all files","*.*")))
		if FILES['save'] == None:
			return
		else:
			FILES['save'].write(self.editor.get("1.0", 'end'))
			FILES['save'].close()

	def Run(self):
		if self.gui_vars['select'] == None:
			messagebox.showerror("Error", "Select a file before pressing 'Run'")
			return
		self.runningbtn.config(background = 'seagreen')
		self.running.set('Running...')
		global FIGURE_URLS
		FIGURE_URLS = self.editor.get("1.0", 'end').split('\n')
		exec(open('main.py').read())
		self.runningbtn.config(background = 'firebrick1')
		self.running.set('Finished.')

Prompt()
