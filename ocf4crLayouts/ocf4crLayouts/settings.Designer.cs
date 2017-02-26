namespace WindowsFormsApplication1
{
    partial class SettingsForm
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(SettingsForm));
            this.settingsCancelButton = new System.Windows.Forms.Button();
            this.settingsSaveButton = new System.Windows.Forms.Button();
            this.explorerSeparateCheckbox = new System.Windows.Forms.CheckBox();
            this.maxWinNumeric = new System.Windows.Forms.NumericUpDown();
            this.maxWinNumericLabel = new System.Windows.Forms.Label();
            this.enableMultipleWindowsCheckbox = new System.Windows.Forms.CheckBox();
            this.multipleGroupBox = new System.Windows.Forms.GroupBox();
            this.ignoreMultipleCheckbox = new System.Windows.Forms.CheckBox();
            this.enableOnlyFirstBookCheckbox = new System.Windows.Forms.CheckBox();
            this.generalGroupBox = new System.Windows.Forms.GroupBox();
            this.customCommandGroupBox = new System.Windows.Forms.GroupBox();
            this.customCommandPartsGroupBox = new System.Windows.Forms.GroupBox();
            this.commandExecutableTextbox = new System.Windows.Forms.TextBox();
            this.commandArgumentsLabel = new System.Windows.Forms.Label();
            this.commandArgumentsTextbox = new System.Windows.Forms.TextBox();
            this.commandExecutableLabel = new System.Windows.Forms.Label();
            this.customCommandLabel2 = new System.Windows.Forms.Label();
            this.customCommandLabel1 = new System.Windows.Forms.Label();
            this.enableCustomCommandCheckbox = new System.Windows.Forms.CheckBox();
            this.explorerExeGroupBox = new System.Windows.Forms.GroupBox();
            this.defaultsButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.maxWinNumeric)).BeginInit();
            this.multipleGroupBox.SuspendLayout();
            this.generalGroupBox.SuspendLayout();
            this.customCommandGroupBox.SuspendLayout();
            this.customCommandPartsGroupBox.SuspendLayout();
            this.explorerExeGroupBox.SuspendLayout();
            this.SuspendLayout();
            // 
            // settingsCancelButton
            // 
            this.settingsCancelButton.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.settingsCancelButton.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.settingsCancelButton.Location = new System.Drawing.Point(12, 560);
            this.settingsCancelButton.Name = "settingsCancelButton";
            this.settingsCancelButton.Size = new System.Drawing.Size(550, 23);
            this.settingsCancelButton.TabIndex = 4;
            this.settingsCancelButton.Text = "Cancel";
            this.settingsCancelButton.UseVisualStyleBackColor = true;
            this.settingsCancelButton.Click += new System.EventHandler(this.settingsCancelButton_Click);
            // 
            // settingsSaveButton
            // 
            this.settingsSaveButton.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.settingsSaveButton.Location = new System.Drawing.Point(12, 502);
            this.settingsSaveButton.Name = "settingsSaveButton";
            this.settingsSaveButton.Size = new System.Drawing.Size(550, 23);
            this.settingsSaveButton.TabIndex = 5;
            this.settingsSaveButton.Text = "Save";
            this.settingsSaveButton.UseVisualStyleBackColor = true;
            this.settingsSaveButton.Click += new System.EventHandler(this.settingsSaveButton_Click);
            // 
            // explorerSeparateCheckbox
            // 
            this.explorerSeparateCheckbox.AutoSize = true;
            this.explorerSeparateCheckbox.Cursor = System.Windows.Forms.Cursors.Default;
            this.explorerSeparateCheckbox.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.explorerSeparateCheckbox.Location = new System.Drawing.Point(6, 19);
            this.explorerSeparateCheckbox.Name = "explorerSeparateCheckbox";
            this.explorerSeparateCheckbox.Size = new System.Drawing.Size(362, 17);
            this.explorerSeparateCheckbox.TabIndex = 0;
            this.explorerSeparateCheckbox.Text = "Open explorer.exe windows in their own separate process (\"/separate\")";
            this.explorerSeparateCheckbox.UseVisualStyleBackColor = true;
            // 
            // maxWinNumeric
            // 
            this.maxWinNumeric.Location = new System.Drawing.Point(6, 19);
            this.maxWinNumeric.Name = "maxWinNumeric";
            this.maxWinNumeric.Size = new System.Drawing.Size(59, 20);
            this.maxWinNumeric.TabIndex = 6;
            this.maxWinNumeric.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // maxWinNumericLabel
            // 
            this.maxWinNumericLabel.AutoSize = true;
            this.maxWinNumericLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.maxWinNumericLabel.Location = new System.Drawing.Point(67, 22);
            this.maxWinNumericLabel.Name = "maxWinNumericLabel";
            this.maxWinNumericLabel.Size = new System.Drawing.Size(253, 13);
            this.maxWinNumericLabel.TabIndex = 7;
            this.maxWinNumericLabel.Text = "Maximum number of windows to open (0 is unlimited)";
            // 
            // enableMultipleWindowsCheckbox
            // 
            this.enableMultipleWindowsCheckbox.AutoSize = true;
            this.enableMultipleWindowsCheckbox.Checked = true;
            this.enableMultipleWindowsCheckbox.CheckState = System.Windows.Forms.CheckState.Checked;
            this.enableMultipleWindowsCheckbox.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.enableMultipleWindowsCheckbox.Location = new System.Drawing.Point(6, 41);
            this.enableMultipleWindowsCheckbox.Name = "enableMultipleWindowsCheckbox";
            this.enableMultipleWindowsCheckbox.Size = new System.Drawing.Size(321, 17);
            this.enableMultipleWindowsCheckbox.TabIndex = 8;
            this.enableMultipleWindowsCheckbox.Text = "Enable opening multiple windows if multiple books are selected";
            this.enableMultipleWindowsCheckbox.UseVisualStyleBackColor = true;
            // 
            // multipleGroupBox
            // 
            this.multipleGroupBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.multipleGroupBox.Controls.Add(this.ignoreMultipleCheckbox);
            this.multipleGroupBox.Controls.Add(this.enableOnlyFirstBookCheckbox);
            this.multipleGroupBox.Controls.Add(this.enableMultipleWindowsCheckbox);
            this.multipleGroupBox.Cursor = System.Windows.Forms.Cursors.Default;
            this.multipleGroupBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.multipleGroupBox.Location = new System.Drawing.Point(6, 45);
            this.multipleGroupBox.Name = "multipleGroupBox";
            this.multipleGroupBox.Size = new System.Drawing.Size(538, 84);
            this.multipleGroupBox.TabIndex = 9;
            this.multipleGroupBox.TabStop = false;
            this.multipleGroupBox.Text = "Multiple Selections";
            // 
            // ignoreMultipleCheckbox
            // 
            this.ignoreMultipleCheckbox.AutoSize = true;
            this.ignoreMultipleCheckbox.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ignoreMultipleCheckbox.Location = new System.Drawing.Point(6, 19);
            this.ignoreMultipleCheckbox.Name = "ignoreMultipleCheckbox";
            this.ignoreMultipleCheckbox.Size = new System.Drawing.Size(269, 17);
            this.ignoreMultipleCheckbox.TabIndex = 10;
            this.ignoreMultipleCheckbox.Text = "Ignore multiple selection - Don\'t open any windowss";
            this.ignoreMultipleCheckbox.UseVisualStyleBackColor = true;
            this.ignoreMultipleCheckbox.CheckedChanged += new System.EventHandler(this.ignoreMultipleCheckbox_Click);
            // 
            // enableOnlyFirstBookCheckbox
            // 
            this.enableOnlyFirstBookCheckbox.AutoSize = true;
            this.enableOnlyFirstBookCheckbox.Enabled = false;
            this.enableOnlyFirstBookCheckbox.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.enableOnlyFirstBookCheckbox.Location = new System.Drawing.Point(6, 64);
            this.enableOnlyFirstBookCheckbox.Name = "enableOnlyFirstBookCheckbox";
            this.enableOnlyFirstBookCheckbox.Size = new System.Drawing.Size(315, 17);
            this.enableOnlyFirstBookCheckbox.TabIndex = 9;
            this.enableOnlyFirstBookCheckbox.Text = "When multiple books are selected only open the first directory";
            this.enableOnlyFirstBookCheckbox.UseVisualStyleBackColor = true;
            // 
            // generalGroupBox
            // 
            this.generalGroupBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.generalGroupBox.Controls.Add(this.maxWinNumeric);
            this.generalGroupBox.Controls.Add(this.multipleGroupBox);
            this.generalGroupBox.Controls.Add(this.maxWinNumericLabel);
            this.generalGroupBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.generalGroupBox.Location = new System.Drawing.Point(12, 12);
            this.generalGroupBox.Name = "generalGroupBox";
            this.generalGroupBox.Size = new System.Drawing.Size(550, 135);
            this.generalGroupBox.TabIndex = 10;
            this.generalGroupBox.TabStop = false;
            this.generalGroupBox.Text = "General Settings";
            // 
            // customCommandGroupBox
            // 
            this.customCommandGroupBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.customCommandGroupBox.Controls.Add(this.customCommandPartsGroupBox);
            this.customCommandGroupBox.Controls.Add(this.customCommandLabel2);
            this.customCommandGroupBox.Controls.Add(this.customCommandLabel1);
            this.customCommandGroupBox.Controls.Add(this.enableCustomCommandCheckbox);
            this.customCommandGroupBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.customCommandGroupBox.Location = new System.Drawing.Point(12, 205);
            this.customCommandGroupBox.Name = "customCommandGroupBox";
            this.customCommandGroupBox.Size = new System.Drawing.Size(550, 291);
            this.customCommandGroupBox.TabIndex = 11;
            this.customCommandGroupBox.TabStop = false;
            this.customCommandGroupBox.Text = "Custom File Explorer Command";
            // 
            // customCommandPartsGroupBox
            // 
            this.customCommandPartsGroupBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.customCommandPartsGroupBox.Controls.Add(this.commandExecutableTextbox);
            this.customCommandPartsGroupBox.Controls.Add(this.commandArgumentsLabel);
            this.customCommandPartsGroupBox.Controls.Add(this.commandArgumentsTextbox);
            this.customCommandPartsGroupBox.Controls.Add(this.commandExecutableLabel);
            this.customCommandPartsGroupBox.Location = new System.Drawing.Point(6, 186);
            this.customCommandPartsGroupBox.Name = "customCommandPartsGroupBox";
            this.customCommandPartsGroupBox.Size = new System.Drawing.Size(538, 99);
            this.customCommandPartsGroupBox.TabIndex = 18;
            this.customCommandPartsGroupBox.TabStop = false;
            this.customCommandPartsGroupBox.Text = "Command";
            // 
            // commandExecutableTextbox
            // 
            this.commandExecutableTextbox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.commandExecutableTextbox.AutoCompleteMode = System.Windows.Forms.AutoCompleteMode.Suggest;
            this.commandExecutableTextbox.AutoCompleteSource = System.Windows.Forms.AutoCompleteSource.FileSystem;
            this.commandExecutableTextbox.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.commandExecutableTextbox.Location = new System.Drawing.Point(6, 32);
            this.commandExecutableTextbox.Name = "commandExecutableTextbox";
            this.commandExecutableTextbox.Size = new System.Drawing.Size(526, 20);
            this.commandExecutableTextbox.TabIndex = 14;
            // 
            // commandArgumentsLabel
            // 
            this.commandArgumentsLabel.AutoSize = true;
            this.commandArgumentsLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.commandArgumentsLabel.Location = new System.Drawing.Point(3, 55);
            this.commandArgumentsLabel.Name = "commandArgumentsLabel";
            this.commandArgumentsLabel.Size = new System.Drawing.Size(371, 13);
            this.commandArgumentsLabel.TabIndex = 17;
            this.commandArgumentsLabel.Text = "Command arguments (\"@path@\" or \"@list\" can be used here - but not both!)";
            // 
            // commandArgumentsTextbox
            // 
            this.commandArgumentsTextbox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.commandArgumentsTextbox.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.commandArgumentsTextbox.Location = new System.Drawing.Point(6, 71);
            this.commandArgumentsTextbox.Name = "commandArgumentsTextbox";
            this.commandArgumentsTextbox.Size = new System.Drawing.Size(526, 20);
            this.commandArgumentsTextbox.TabIndex = 16;
            // 
            // commandExecutableLabel
            // 
            this.commandExecutableLabel.AutoSize = true;
            this.commandExecutableLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.commandExecutableLabel.Location = new System.Drawing.Point(3, 16);
            this.commandExecutableLabel.Name = "commandExecutableLabel";
            this.commandExecutableLabel.Size = new System.Drawing.Size(355, 13);
            this.commandExecutableLabel.TabIndex = 15;
            this.commandExecutableLabel.Text = "Command executable (must exist on disk; i.e. \"C:\\Windows\\explorer.exe\")";
            // 
            // customCommandLabel2
            // 
            this.customCommandLabel2.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.customCommandLabel2.Location = new System.Drawing.Point(16, 88);
            this.customCommandLabel2.Name = "customCommandLabel2";
            this.customCommandLabel2.Size = new System.Drawing.Size(528, 72);
            this.customCommandLabel2.TabIndex = 13;
            this.customCommandLabel2.Text = resources.GetString("customCommandLabel2.Text");
            // 
            // customCommandLabel1
            // 
            this.customCommandLabel1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.customCommandLabel1.Location = new System.Drawing.Point(6, 16);
            this.customCommandLabel1.Name = "customCommandLabel1";
            this.customCommandLabel1.Size = new System.Drawing.Size(538, 70);
            this.customCommandLabel1.TabIndex = 12;
            this.customCommandLabel1.Text = resources.GetString("customCommandLabel1.Text");
            // 
            // enableCustomCommandCheckbox
            // 
            this.enableCustomCommandCheckbox.AutoSize = true;
            this.enableCustomCommandCheckbox.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.enableCustomCommandCheckbox.Location = new System.Drawing.Point(6, 163);
            this.enableCustomCommandCheckbox.Name = "enableCustomCommandCheckbox";
            this.enableCustomCommandCheckbox.Size = new System.Drawing.Size(147, 17);
            this.enableCustomCommandCheckbox.TabIndex = 11;
            this.enableCustomCommandCheckbox.Text = "Enable Custom Command";
            this.enableCustomCommandCheckbox.UseVisualStyleBackColor = true;
            this.enableCustomCommandCheckbox.CheckedChanged += new System.EventHandler(this.enableCustomCommandCheckbox_Click);
            // 
            // explorerExeGroupBox
            // 
            this.explorerExeGroupBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.explorerExeGroupBox.Controls.Add(this.explorerSeparateCheckbox);
            this.explorerExeGroupBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.explorerExeGroupBox.Location = new System.Drawing.Point(12, 153);
            this.explorerExeGroupBox.Name = "explorerExeGroupBox";
            this.explorerExeGroupBox.Size = new System.Drawing.Size(550, 46);
            this.explorerExeGroupBox.TabIndex = 12;
            this.explorerExeGroupBox.TabStop = false;
            this.explorerExeGroupBox.Text = "explorer.exe";
            // 
            // defaultsButton
            // 
            this.defaultsButton.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.defaultsButton.Location = new System.Drawing.Point(12, 531);
            this.defaultsButton.Name = "defaultsButton";
            this.defaultsButton.Size = new System.Drawing.Size(550, 23);
            this.defaultsButton.TabIndex = 13;
            this.defaultsButton.Text = "Defaults";
            this.defaultsButton.UseVisualStyleBackColor = true;
            // 
            // SettingsForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.settingsCancelButton;
            this.ClientSize = new System.Drawing.Size(574, 595);
            this.Controls.Add(this.defaultsButton);
            this.Controls.Add(this.explorerExeGroupBox);
            this.Controls.Add(this.customCommandGroupBox);
            this.Controls.Add(this.generalGroupBox);
            this.Controls.Add(this.settingsSaveButton);
            this.Controls.Add(this.settingsCancelButton);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(3000, 634);
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(590, 634);
            this.Name = "SettingsForm";
            this.ShowInTaskbar = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
            this.Text = "Open Containing Folder for ComicRack Settings";
            ((System.ComponentModel.ISupportInitialize)(this.maxWinNumeric)).EndInit();
            this.multipleGroupBox.ResumeLayout(false);
            this.multipleGroupBox.PerformLayout();
            this.generalGroupBox.ResumeLayout(false);
            this.generalGroupBox.PerformLayout();
            this.customCommandGroupBox.ResumeLayout(false);
            this.customCommandGroupBox.PerformLayout();
            this.customCommandPartsGroupBox.ResumeLayout(false);
            this.customCommandPartsGroupBox.PerformLayout();
            this.explorerExeGroupBox.ResumeLayout(false);
            this.explorerExeGroupBox.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion
        private System.Windows.Forms.Button settingsCancelButton;
        private System.Windows.Forms.Button settingsSaveButton;
        private System.Windows.Forms.CheckBox explorerSeparateCheckbox;
        private System.Windows.Forms.NumericUpDown maxWinNumeric;
        private System.Windows.Forms.Label maxWinNumericLabel;
        private System.Windows.Forms.CheckBox enableMultipleWindowsCheckbox;
        private System.Windows.Forms.GroupBox multipleGroupBox;
        private System.Windows.Forms.CheckBox enableOnlyFirstBookCheckbox;
        private System.Windows.Forms.GroupBox generalGroupBox;
        private System.Windows.Forms.CheckBox ignoreMultipleCheckbox;
        private System.Windows.Forms.GroupBox customCommandGroupBox;
        private System.Windows.Forms.GroupBox explorerExeGroupBox;
        private System.Windows.Forms.Label customCommandLabel1;
        private System.Windows.Forms.CheckBox enableCustomCommandCheckbox;
        private System.Windows.Forms.Label customCommandLabel2;
        private System.Windows.Forms.Label commandExecutableLabel;
        private System.Windows.Forms.TextBox commandExecutableTextbox;
        private System.Windows.Forms.Label commandArgumentsLabel;
        private System.Windows.Forms.TextBox commandArgumentsTextbox;
        private System.Windows.Forms.GroupBox customCommandPartsGroupBox;
        private System.Windows.Forms.Button defaultsButton;
    }
}