// Introducing C++ Classes, pp.270-272
// The general form of a simple class declaration, p.272
/*
class class-name
{
  private date and functions
public:
  public data and functions
}  object name list;
*/

// pp.270-271
#define SIZE 100
//This creates the class stack.
class stack{
  int stck[SIZE]
  int tos;
public:
  void int();
  void push( int i);
  int  pop();
};

// p.272
void stack::push(int i)
{
  if ( tos==SIZE )
  {
    cout << "Stack is full" << endl;
  }
  stck[tos] = id;
  tos++;
}
