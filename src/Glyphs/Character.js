import Glyph from "./Glyph.js";

class Character extends Glyph {
  constructor(unicode, symbol, normal, cset) {
    super(unicode, symbol);
    this.normal = normal;
    this.character_set = cset;
  }
}

export default Character;
