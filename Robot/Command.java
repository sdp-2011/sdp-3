public class Command {

  int type;
  short argument;

  public Command(int type) {
    this.type = type;
  }

  public Command(int type, short argument) {
    this.type = type;
    this.argument = argument;
  }

  public int getType() {
    return type;
  }

  public void setType(int type) {
    this.type = type;
  }

  public short getArgument() {
    return argument;
  }

  public void setArgument(short argument) {
    this.argument = argument;
  }

  public boolean hasArgument() {
    return argument != 0;
  }

}
