import Fraktur from "./Fonts/Fraktur.js";
import SansSerif from "./Fonts/SansSerif.js";
import DoubleStruck from "./Fonts/DoubleStruck.js";
import Script from "./Fonts/Script.js";
import Serif from "./Fonts/Serif.js";
import Monospace from "./Fonts/Monospace.js";
import {extraFonts} from "./Fonts/allFonts.js";

class FontManager {
    constructor() {
      this.fonts = {
        Fraktur: Fraktur,
        SansSerif: SansSerif,
        Serif: Serif,
        Script: Script,
        Monospace: Monospace,
        DoubleStruck: DoubleStruck,
        ...extraFonts
      };
  
      this.valid_fonts = [
        "Fraktur",
        "SansSerif",
        "Serif",
        "Script",
        "Monospace",
        "DoubleStruck",
        ...Object.keys(extraFonts)
      ];
    }

    getGlyph(font,style,input){
      if(this.fonts.hasOwnProperty(font)){
        style = style !== "normal" && this.fonts[font].hasStyle(style)? style : "normal";
        if(font === "Serif" && style === "normal") return input; 
        const cset = this.fonts[font].character_sets[style];

        return cset.hasCharacter(input)? cset.getSymbol(input) : input; 
      }

      return input; 
    }
  
    write(font, style, input) {
      if (this.fonts.hasOwnProperty(font)) {
        style =
          style !== "normal" && this.fonts[font].hasStyle(style)
            ? style
            : "normal";
  
        if (font === "Serif" && style === "normal") return input;
        const cset = this.fonts[font].character_sets[style];
        let str = "";
        for (let i = 0; i < input.length; i++) {
          const ch = input[i];
          str += cset.hasCharacter(ch) ? cset.getSymbol(ch) : ch;
        }
  
        return str;
      }
  
      return input;
    }
  }
  
  const font_manager = new FontManager();
  
  export default font_manager;