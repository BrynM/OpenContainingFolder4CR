namespace WindowsFormsApplication1
{
    partial class MultipleDirsForm
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
            this.selectAllCheckbox = new System.Windows.Forms.CheckBox();
            this.openButton = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.directoryCheckboxes = new System.Windows.Forms.CheckedListBox();
            this.labelMessage = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // selectAllCheckbox
            // 
            this.selectAllCheckbox.AutoSize = true;
            this.selectAllCheckbox.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.selectAllCheckbox.Location = new System.Drawing.Point(12, 57);
            this.selectAllCheckbox.Name = "selectAllCheckbox";
            this.selectAllCheckbox.Size = new System.Drawing.Size(80, 17);
            this.selectAllCheckbox.TabIndex = 0;
            this.selectAllCheckbox.Text = "Select All";
            this.selectAllCheckbox.UseVisualStyleBackColor = true;
            // 
            // openButton
            // 
            this.openButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.openButton.AutoSize = true;
            this.openButton.Location = new System.Drawing.Point(15, 364);
            this.openButton.Name = "openButton";
            this.openButton.Size = new System.Drawing.Size(703, 23);
            this.openButton.TabIndex = 2;
            this.openButton.Text = "Open selected directories...";
            this.openButton.UseVisualStyleBackColor = true;
            this.openButton.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.button2.Location = new System.Drawing.Point(15, 393);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(703, 23);
            this.button2.TabIndex = 3;
            this.button2.Text = "Cancel";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // directoryCheckboxes
            // 
            this.directoryCheckboxes.FormattingEnabled = true;
            this.directoryCheckboxes.Items.AddRange(new object[] {
            "foo",
            "bar",
            "baz"});
            this.directoryCheckboxes.Location = new System.Drawing.Point(12, 80);
            this.directoryCheckboxes.Name = "directoryCheckboxes";
            this.directoryCheckboxes.Size = new System.Drawing.Size(703, 274);
            this.directoryCheckboxes.TabIndex = 1;
            // 
            // labelMessage
            // 
            this.labelMessage.AutoSize = true;
            this.labelMessage.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelMessage.ForeColor = System.Drawing.SystemColors.Highlight;
            this.labelMessage.Location = new System.Drawing.Point(12, 9);
            this.labelMessage.Name = "labelMessage";
            this.labelMessage.Size = new System.Drawing.Size(567, 39);
            this.labelMessage.TabIndex = 4;
            this.labelMessage.Text = "Multiple directories found. Please select the ones you which to open.\r\n\r\nWarning!" +
    " This could open many windows at once and may be slow for large numbers of direc" +
    "tories.";
            // 
            // MultipleDirsForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(730, 428);
            this.Controls.Add(this.labelMessage);
            this.Controls.Add(this.directoryCheckboxes);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.openButton);
            this.Controls.Add(this.selectAllCheckbox);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(2500, 2000);
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(746, 467);
            this.Name = "MultipleDirsForm";
            this.Text = "Open Containing Folder for ComicRack";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.CheckBox selectAllCheckbox;
        private System.Windows.Forms.Button openButton;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.CheckedListBox directoryCheckboxes;
        private System.Windows.Forms.Label labelMessage;
    }
}

