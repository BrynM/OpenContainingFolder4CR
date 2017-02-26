import clr
import System
clr.AddReference("System.Drawing")
import System.Drawing
clr.AddReference("System.Windows.Forms")
clr.AddReference("PresentationFramework")
clr.AddReference("PresentationCore")
from System.Windows.Interop import WindowInteropHelper

import System.IO
from System.IO import StreamWriter, TextWriter

import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from System.Collections import *

from globalvars import *

class MultipleDirsForm(Form):

	def __init__(self, dirList):
		self._dirList = dirList
		self.InitializeComponent(dirList)


	def InitializeComponent(self, dirList):
		#self._Cancel = System.Windows.Forms.Button()
		#self.SuspendLayout()
		#self.ResumeLayout(False)
		self.checkBox1 = System.Windows.Forms.CheckBox();
		self.button1 = System.Windows.Forms.Button();
		self.button2 = System.Windows.Forms.Button();
		self.checkedListBox1 = System.Windows.Forms.CheckedListBox();
		self.SuspendLayout();
		#
		# label1
		#
		this.label1.AutoSize = true;
		this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
		this.label1.ForeColor = System.Drawing.SystemColors.Highlight;
		this.label1.Location = new System.Drawing.Point(12, 9);
		this.label1.Name = "label1";
		this.label1.Size = new System.Drawing.Size(567, 39);
		this.label1.Text = "Multiple directories found. Please select the ones you which to open.\n\nWarning! This could open many windows at once and may be slow for large numbers of directories."
		#
		# checkBox1
		#
		self.checkBox1.AutoSize = True;
		self.checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
		self.checkBox1.Location = System.Drawing.Point(12, 57);
		self.checkBox1.Name = "checkBox1";
		self.checkBox1.Size = System.Drawing.Size(80, 17);
		self.checkBox1.TabIndex = 0;
		self.checkBox1.Text = "Select All";
		self.checkBox1.UseVisualStyleBackColor = True;
		#
		# checkedListBox1
		#
		self.checkedListBox1.FormattingEnabled = True;
		#self.checkedListBox1.Items.AddRange(set(dirList));
		self.checkedListBox1.Location = System.Drawing.Point(12, 80);
		self.checkedListBox1.Name = "checkedListBox1";
		self.checkedListBox1.Size = System.Drawing.Size(703, 274);
		self.checkedListBox1.TabIndex = 1;
		#
		# button1
		#
		self.button1.Location = System.Drawing.Point(15, 364);
		self.button1.Name = "button1";
		self.button1.Size = System.Drawing.Size(703, 23);
		self.button1.TabIndex = 2;
		self.button1.Text = "Open selected directories...";
		self.button1.UseVisualStyleBackColor = True;
#		self.button1.Click += System.EventHandler(self.button1_Click);
		#
		# button2
		#
		self.button2.Location = System.Drawing.Point(15, 393);
		self.button2.Name = "button2";
		self.button2.Size = System.Drawing.Size(703, 23);
		self.button2.TabIndex = 3;
		self.button2.Text = "Cancel";
		self.button2.UseVisualStyleBackColor = True;
#		self.button2.Click += System.EventHandler(self.button2_Click);
		#
		# Form1
		#
		#self.AutoScaleDimensions = System.Drawing.SizeF(6F, 13F);
		self.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
		self.ClientSize = System.Drawing.Size(730, 428);
		self.Controls.Add(self.label1);
		self.Controls.Add(self.checkedListBox1);
		self.Controls.Add(self.button2);
		self.Controls.Add(self.button1);
		self.Controls.Add(self.checkBox1);
		self.Name = "Form1";
		self.Text = "Open Containing Folder for ComicRack";
		self.ResumeLayout(False);
		self.PerformLayout();


"""
namespace WindowsFormsApplication1
{
	partial class Form1
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Windows Form Designer generated code

		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.checkBox1 = new System.Windows.Forms.CheckBox();
			this.button1 = new System.Windows.Forms.Button();
			this.button2 = new System.Windows.Forms.Button();
			this.checkedListBox1 = new System.Windows.Forms.CheckedListBox();
			this.SuspendLayout();
			//
			// checkBox1
			//
			this.checkBox1.AutoSize = true;
			this.checkBox1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.checkBox1.Location = new System.Drawing.Point(12, 57);
			this.checkBox1.Name = "checkBox1";
			this.checkBox1.Size = new System.Drawing.Size(80, 17);
			this.checkBox1.TabIndex = 0;
			this.checkBox1.Text = "Select All";
			this.checkBox1.UseVisualStyleBackColor = true;
			//
			// button1
			//
			this.button1.Location = new System.Drawing.Point(15, 364);
			this.button1.Name = "button1";
			this.button1.Size = new System.Drawing.Size(703, 23);
			this.button1.TabIndex = 2;
			this.button1.Text = "Open selected directories...";
			this.button1.UseVisualStyleBackColor = true;
			this.button1.Click += new System.EventHandler(this.button1_Click);
			//
			// button2
			//
			this.button2.Location = new System.Drawing.Point(15, 393);
			this.button2.Name = "button2";
			this.button2.Size = new System.Drawing.Size(703, 23);
			this.button2.TabIndex = 3;
			this.button2.Text = "Cancel";
			this.button2.UseVisualStyleBackColor = true;
			this.button2.Click += new System.EventHandler(this.button2_Click);
			//
			// checkedListBox1
			//
			this.checkedListBox1.FormattingEnabled = true;
			this.checkedListBox1.Items.AddRange(new object[] {
			"foo",
			"bar",
			"baz"});
			this.checkedListBox1.Location = new System.Drawing.Point(12, 80);
			this.checkedListBox1.Name = "checkedListBox1";
			this.checkedListBox1.Size = new System.Drawing.Size(703, 274);
			this.checkedListBox1.TabIndex = 1;
			//
			// Form1
			//
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(730, 428);
			this.Controls.Add(this.checkedListBox1);
			this.Controls.Add(this.button2);
			this.Controls.Add(this.button1);
			this.Controls.Add(this.checkBox1);
			this.Name = "Form1";
			this.Text = "Open Containing Folder for ComicRack";
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.CheckBox checkBox1;
		private System.Windows.Forms.Button button1;
		private System.Windows.Forms.Button button2;
		private System.Windows.Forms.CheckedListBox checkedListBox1;
	}
}

"""