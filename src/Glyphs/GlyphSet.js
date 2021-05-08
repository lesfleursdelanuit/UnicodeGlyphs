import Glyph from "./Glyph.js";
class GlyphSet {
  constructor(name, id) {
    this.id = id;
    this.name = name;
    this.glyphs = {};
  }

  addGlyph(ucode, symbol) {
    this.glyphs[ucode] = new Glyph(ucode, symbol);
  }

  getSymbolSet() {
    let symbols = [];
    for (let key in this.glyphs) symbols.push(this.glyphs[key].symbol);
    return symbols;
  }
}

export default GlyphSet;