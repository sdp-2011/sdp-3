/*

This is an example topic 

It supplies two main components, an object (TimeOfDay) and an interface (Hello).

The object is a specification of something that can be passed between the server and the client.

The interface is a specification of methods which can be called or objects shadered.

*/
module Demo
{
    struct TimeOfDay
    {
        short hour;   // 0 - 23
        short minute; // 0 - 59
        short second; // 0 - 59
    };

    interface Hello
    {
        void sayHello(string s);
        TimeOfDay getTime();
    };
};
