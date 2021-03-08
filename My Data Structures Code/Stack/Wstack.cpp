// IMPLEMENTING BASIC STACK BEHVIOUR

#include <iostream>
using namespace std;

int stack[100], n = 100, top = -1;

void push(int val)
{
    if (top > n - 1)
    {
        cout << "The stack is overflowing" << endl;
    }
    else
    {
        // cout << "Enter a value to push " << endl;
        // cin >> val;
        top++;
        stack[top] = val;
    }
}

void peek()
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

void pop() 
{
    if(top < 0) {
        cout<<"The Stack is empty"<<endl;
    } else {
        cout<<"The popped element is "<< stack[top]<<endl; 
        top--;
    }
}

int main()
{
    int ch, val;
    cout << "1) Push in stack" << endl;
    cout << "2) Pop from stack" << endl;
    cout << "3) Display stack" << endl;
    cout << "4) Exit" << endl;
    do
    {
        cout << "Enter choice: " << endl;
        cin >> ch;
        switch (ch)
        {
        case 1:
        {
            cout << "Enter value to be pushed:" << endl;
            cin >> val;
            push(val);
            break;
        }
        case 2:
        {
            pop();
            break;
        }
        case 3:
        {
            peek();
            break;
        }
        case 4:
        {
            cout << "Exit" << endl;
            break;
        }
        default:
        {
            cout << "Invalid Choice" << endl;
        }
        }
    } while (ch != 4);
    return 0;
}
