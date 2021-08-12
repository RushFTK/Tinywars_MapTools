
namespace TinywarsMapScriptEditor
{
    partial class form1
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要修改
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.textbox_sourceinfo = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.label_username = new System.Windows.Forms.Label();
            this.textBox_username = new System.Windows.Forms.TextBox();
            this.label_password = new System.Windows.Forms.Label();
            this.textBox_password = new System.Windows.Forms.TextBox();
            this.label_pwencrypt = new System.Windows.Forms.Label();
            this.textBox_pwencrypt = new System.Windows.Forms.TextBox();
            this.button_login = new System.Windows.Forms.Button();
            this.webBrowser1 = new System.Windows.Forms.WebBrowser();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // textbox_sourceinfo
            // 
            this.textbox_sourceinfo.Location = new System.Drawing.Point(12, 202);
            this.textbox_sourceinfo.Multiline = true;
            this.textbox_sourceinfo.Name = "textbox_sourceinfo";
            this.textbox_sourceinfo.Size = new System.Drawing.Size(763, 236);
            this.textbox_sourceinfo.TabIndex = 0;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(172, 23);
            this.button1.TabIndex = 1;
            this.button1.Text = "Get Script Source Code";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // label_username
            // 
            this.label_username.AutoSize = true;
            this.label_username.Location = new System.Drawing.Point(453, 44);
            this.label_username.Name = "label_username";
            this.label_username.Size = new System.Drawing.Size(53, 12);
            this.label_username.TabIndex = 2;
            this.label_username.Text = "Username";
            // 
            // textBox_username
            // 
            this.textBox_username.Location = new System.Drawing.Point(560, 41);
            this.textBox_username.Name = "textBox_username";
            this.textBox_username.Size = new System.Drawing.Size(215, 21);
            this.textBox_username.TabIndex = 3;
            // 
            // label_password
            // 
            this.label_password.AutoSize = true;
            this.label_password.Location = new System.Drawing.Point(453, 77);
            this.label_password.Name = "label_password";
            this.label_password.Size = new System.Drawing.Size(53, 12);
            this.label_password.TabIndex = 4;
            this.label_password.Text = "password";
            // 
            // textBox_password
            // 
            this.textBox_password.Location = new System.Drawing.Point(560, 74);
            this.textBox_password.Name = "textBox_password";
            this.textBox_password.Size = new System.Drawing.Size(215, 21);
            this.textBox_password.TabIndex = 5;
            this.textBox_password.Leave += new System.EventHandler(this.textBox_password_Leave);
            // 
            // label_pwencrypt
            // 
            this.label_pwencrypt.AutoSize = true;
            this.label_pwencrypt.Location = new System.Drawing.Point(453, 160);
            this.label_pwencrypt.Name = "label_pwencrypt";
            this.label_pwencrypt.Size = new System.Drawing.Size(101, 12);
            this.label_pwencrypt.TabIndex = 6;
            this.label_pwencrypt.Text = "password_encrypt";
            // 
            // textBox_pwencrypt
            // 
            this.textBox_pwencrypt.Location = new System.Drawing.Point(560, 157);
            this.textBox_pwencrypt.Name = "textBox_pwencrypt";
            this.textBox_pwencrypt.Size = new System.Drawing.Size(215, 21);
            this.textBox_pwencrypt.TabIndex = 7;
            // 
            // button_login
            // 
            this.button_login.Location = new System.Drawing.Point(700, 117);
            this.button_login.Name = "button_login";
            this.button_login.Size = new System.Drawing.Size(75, 23);
            this.button_login.TabIndex = 8;
            this.button_login.Text = "log in";
            this.button_login.UseVisualStyleBackColor = true;
            // 
            // webBrowser1
            // 
            this.webBrowser1.Location = new System.Drawing.Point(12, 41);
            this.webBrowser1.Margin = new System.Windows.Forms.Padding(0);
            this.webBrowser1.MinimumSize = new System.Drawing.Size(20, 20);
            this.webBrowser1.Name = "webBrowser1";
            this.webBrowser1.ScriptErrorsSuppressed = true;
            this.webBrowser1.Size = new System.Drawing.Size(414, 145);
            this.webBrowser1.TabIndex = 9;
            this.webBrowser1.Url = new System.Uri("https://tinywars.online/game/legacy/index.html", System.UriKind.Absolute);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(560, 185);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(179, 12);
            this.label1.TabIndex = 10;
            this.label1.Text = "\"NVQvwpVCNpaafM9olxl2dWrhGN0\"";
            // 
            // form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.webBrowser1);
            this.Controls.Add(this.button_login);
            this.Controls.Add(this.textBox_pwencrypt);
            this.Controls.Add(this.label_pwencrypt);
            this.Controls.Add(this.textBox_password);
            this.Controls.Add(this.label_password);
            this.Controls.Add(this.textBox_username);
            this.Controls.Add(this.label_username);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.textbox_sourceinfo);
            this.Name = "form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox textbox_sourceinfo;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label_username;
        private System.Windows.Forms.TextBox textBox_username;
        private System.Windows.Forms.Label label_password;
        private System.Windows.Forms.TextBox textBox_password;
        private System.Windows.Forms.Label label_pwencrypt;
        private System.Windows.Forms.TextBox textBox_pwencrypt;
        private System.Windows.Forms.Button button_login;
        private System.Windows.Forms.WebBrowser webBrowser1;
        private System.Windows.Forms.Label label1;
    }
}

