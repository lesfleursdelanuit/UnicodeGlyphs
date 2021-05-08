import CharacterSet from "../CharacterSet.js";
const styles = ["normal", "italic", "bold italic", "bold"];
class Font {
  constructor(id, name) {
    this.id = id;
    this.name = name;
    this.character_sets = {};
    for (let i = 0; i < styles.length; i++)
      this.character_sets[styles[i]] = null;
  }
  hasStyle(style) {
    return (
      this.character_sets.hasOwnProperty(style) &&
      this.character_sets[style] !== null
    );
  }

  initCharacterSet(style, id) {
    this.character_sets[style] = new CharacterSet(this, style, id);
  }
}

export default Font;
