/**
 * Enumeration that represents a command - forward, backward,
 * stop, etc.
 *
 * @author Stephen McGruer
 */
public enum Command {

  QUIT(0),
  FORWARD(1),
  BACKWARD(2),
  STOP(3),
  LEFT(4),
  RIGHT(5),
  KICK(6),
  SETLEFTMOTOR(7),
  SETRIGHTMOTOR(8);

  /* Tracks the index of the Command */
  private int index;

  /**
   * Private constructor sets the index.
   *
   * @param index   The index of the command.
   */
  private Command(int index) {
    this.index = index;
  }

  /**
   * Returns the index of a Command enum value.
   *
   * @return      The index of the Command.
   */
  public int getIndex() {
    return this.index;
  }

}
