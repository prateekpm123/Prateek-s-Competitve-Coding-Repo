// A PROBLEM FROM PEP CODING.COM

#include <iostream>
using namespace std;

int top = -1;

void push(int val, int stack[])
{
    // if (top > n - 1)
    // {
    //     cout << "The stack is overflowing" << endl;
    // }
    // else
    // {
    //     // cout << "Enter a value to push " << endl;
    //     // cin >> val;
    top++;
    stack[top] = val;
    // }
}

void peek(int stack[])
{
    if (top >= 0)
    {
        for (int i = 0; i <= top; i++)
        {
            cout << stack[i] << " ";
        }
    }
    else
    {
        cout << "Stack is empty" << endl;
    }
}

void pop(int stack[])
{
    if (top < 0)
    {
        cout << "The Stack is empty" << endl;
    }
    else
    {
        cout << "The popped element is " << stack[top] << endl;
        top--;
    }
}

int main()
{
    string str1 = "(a+b) + ((c+d)-e)";
    cout << "This is given expression" << endl;
    cout << str1;
    int stack[300];

    for (int i = 0; i < str1.length(); i++)
    {
        cout<<"in for loop";
        char ch = str1[i];
        int len = sizeof(stack);

        if (ch == ')')
        {
            if (stack[len - 1] == '(')
            {
                cout << "true" << endl;
            }
            else
            {
                while (stack[len - 1] != '(')
                {
                    pop(stack);
                }
            }
        } else {
            push(ch, stack);
        }
    }
    cout<<"false"<<endl;
}