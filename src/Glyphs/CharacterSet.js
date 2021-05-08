import Character from "./Character.js";
import GlyphSet from "./GlyphSet.js";
const letters = "abcdefghijklmnopqrstuvwxyz";
const digits = "0123456789";

class CharacterSets extends GlyphSet {
  constructor(font, style, id) {
    super(font, id);
    this.font = font;
    this.style = style;
    this.characters = {};
    for (let i = 0; i < letters.length; i++) {
      this.characters[letters[i]] = null;
      this.characters[letters[i].toUpperCase()] = null;
    }

    for (let i = 0; i < digits.length; i++) this.characters[digits[i]] = null;
  }

  getSymbol(ch) {
    return this.characters[ch].symbol;
  }

  hasCharacter(char) {
    return (
      this.characters.hasOwnProperty(char) && this.characters[char] !== null
    );
  }

  setCharacter(unicode, c, symbol) {
    this.characters[c] = new Character(unicode, symbol, c, this);
    //this.addGlyph(unicode, symbol);
  }
}

export default CharacterSets;