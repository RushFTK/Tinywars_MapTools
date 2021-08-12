using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TinywarsMapScriptEditor
{
    public partial class form1 : Form
    {
        public form1()
        {
            InitializeComponent();
        }

        private void textBox_password_Leave(object sender, EventArgs e)
        {
            string source_passoword = textBox_password.Text;
            using (SHA1 sha1 = SHA1CryptoServiceProvider.Create())
            {
                byte[] textBytes = System.Text.Encoding.UTF8.GetBytes(textBox_password.Text);
                byte[] hashBytes = sha1.ComputeHash(textBytes);
                string prepared = Encoding.UTF8.GetString(hashBytes);
                textBox_pwencrypt.Text = prepared;
            }           
        }
    }
}
