using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class SettingsForm : Form
    {
        public SettingsForm()
        {
            InitializeComponent();
            ignoreMultipleCheckbox_Click(null, null);
            enableCustomCommandCheckbox_Click(null, null);
        }

        private void settingsCancelButton_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void settingsSaveButton_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void ignoreMultipleCheckbox_Click(object sender, EventArgs e)
        {
            if (this.ignoreMultipleCheckbox.Checked)
            {
                this.enableMultipleWindowsCheckbox.Enabled = false;
                this.enableOnlyFirstBookCheckbox.Enabled = false;
            }
            else
            {
                this.enableMultipleWindowsCheckbox.Enabled = true;
                this.enableOnlyFirstBookCheckbox.Enabled = true;
            }
        }

        private void enableCustomCommandCheckbox_Click(object sender, EventArgs e)
        {
            if (this.enableCustomCommandCheckbox.Checked)
            {
                this.explorerExeGroupBox.Enabled = false;
                this.customCommandPartsGroupBox.Enabled = true;
            }
            else
            {
                this.explorerExeGroupBox.Enabled = true;
                this.customCommandPartsGroupBox.Enabled = false;
            }
        }
        
    }
}
