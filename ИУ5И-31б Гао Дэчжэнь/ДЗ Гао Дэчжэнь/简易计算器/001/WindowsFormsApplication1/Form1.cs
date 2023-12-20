using System;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        //存储上次点击了什么按钮，0代表什么都没有点击，1代表数字按钮，2代表点击了运算符,3代表点击.
        //Stores what button was clicked last time, 0 means nothing was clicked, 1 means a numeric button, 2 means an operator was clicked, 3 means a click.
        private int prev = 0;
        //存储计算的中间结果
        //Storing intermediate results of calculations
        private decimal zjjg = 0;
        //记录上次按得什么运算符
        //Record what operator was last pressed
        private string prevysf = "+";

        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            txtbottom.Text = "";
            txttop.Text = "";
        }
        private void button1_Click(object sender, EventArgs e) //输入的数 Number of inputs
        {
            //将事件源转换为按钮
            //Converting event sources to buttons
            Button btn = sender as Button;
            //替换(文本框内容为0，点击了运算符)
            //Replace (text box content 0, operator clicked)
            if (prev == 2 || txtbottom.Text == "0")
            {
                txtbottom.Text = btn.Text;
                txttop.Text += btn.Text;//进行显示拼接 Perform display splicing
            }
            //追加(内容不为0，并且上次没有点击运算符)
            //Append (content is not 0 and operator was not clicked last time)
            else
            {
                txtbottom.Text +=btn.Text;
                txttop.Text += btn.Text;//进行显示拼接
            }
            //点击了按钮数字Clicked on the button numbers
            prev = 1;
        }
        
        private void button2_dot_Click(object sender, EventArgs e)//输入 点
        {
            if (prev == 0 || prev == 2)
            {
                txtbottom.Text = "0.";
                txttop.Text += "0.";//进行显示拼接Perform display splicing
            }
            else if (txtbottom.Text == "0.")
            {
                txtbottom.Text = "0.";
            }
            else if (prev == 3)
            {
                txtbottom.Text = txtbottom.Text;
                txttop.Text = txttop.Text;//进行显示拼接
            }
            else
            {
                txtbottom.Text += ".";
                txttop.Text += ".";//进行显示拼接
            }
            prev = 3;
        }
        private void button4_Click(object sender, EventArgs e) //加减乘除addition, subtraction, multiplication and division
        {
            //事件源转换为按钮Event Source Conversion to Button
            Button btn = sender as Button;
            //上次按了数字
            if (prev == 1)
            {
                txttop.Text += btn.Text;//进行显示拼接
                switch (prevysf)
                {
                    case "+":
                        zjjg = zjjg + Convert.ToDecimal(txtbottom.Text); //计算上次运行的结果
                        break;
                    case "-":
                        zjjg = zjjg - Convert.ToDecimal(txtbottom.Text); //计算上次运行的结果
                        break;
                    case "*":
                        zjjg = zjjg * Convert.ToDecimal(txtbottom.Text); //计算上次运行的结果
                        break;
                    case "/":
                        zjjg = zjjg / Convert.ToDecimal(txtbottom.Text); //计算上次运行的结果
                        break;                   
                }

                txtbottom.Text = zjjg.ToString();
            }
            //上次按了运算符
            else
            {
                if (txttop.Text != "")
                {
                    string s = txttop.Text;
                    s = s.Substring(0, s.Length - 1);
                    s = s + btn.Text;
                    txttop.Text = s;
                }
                else
                {
                    txttop.Text = txtbottom.Text + btn.Text;
                }
            }
            //点击了运算符
            prev = 2;
            //记录下运算符
            prevysf = btn.Text;
        }

        private void button9_Click(object sender, EventArgs e) //清空
        {
            txttop.Text = "";
            txtbottom.Text = "";
            prevysf = "+";
            prev = 0;
            zjjg = 0;
        }

        private void button11_Click(object sender, EventArgs e) //等于
        {

            //上次按了数字
            if (prev == 1)
            {
                txttop.Text += "=";//进行显示拼接  
                //事件源转换为按钮
                Button btn = sender as Button;
                switch (prevysf)
                {
                    case "+":
                        try
                        {
                            zjjg = zjjg + Convert.ToDecimal(txtbottom.Text); //计算上次运行的结果Calculate the results of the last run
                        }
                        catch (Exception)
                        {
                            zjjg = 0;
                        }
                        break;
                    case "-":
                        zjjg = zjjg - Convert.ToDecimal(txtbottom.Text); //计算上次运行的结果Calculate the results of the last run
                        break;
                    case "*":
                        zjjg = zjjg * Convert.ToDecimal(txtbottom.Text); //计算上次运行的结果Calculate the results of the last run
                        break;
                    case "/":
                        zjjg = zjjg / Convert.ToDecimal(txtbottom.Text); //计算上次运行的结果Calculate the results of the last run
                        break;
                    default:
                        zjjg = 0;
                        break;
                }
                txtbottom.Text = zjjg.ToString();
                prevysf = "";
                prev = 2;
            }
            if (txtbottom.Text=="0.")
            {
                txtbottom.Text = "";
                prevysf = "";
                prev = 2;
            }            
        }

        private void button17_Click(object sender, EventArgs e) //回退一个Go back one
        {
            IsMoney(txtbottom.Text);   

        }
        public static bool IsMoney(string input)
        {
            string pattern = @"^\-{0,1}[0-9]{0,}\.{0,1}[0-9]{1,}$";
            return System.Text.RegularExpressions.Regex.IsMatch(input, pattern, System.Text.RegularExpressions.RegexOptions.IgnoreCase);
        }
    }
}
