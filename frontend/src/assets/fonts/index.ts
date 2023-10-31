class Font {
  constructor(
    public fname: string,
    public fstyle: string,
    public fweight: number,
    public furl: string
  ) {
    this.fname = fname;
    this.fstyle = fstyle;
    this.fweight = fweight;
    this.furl = furl;
  }

  getFontConfig() {
    return {
      fontFamily: this.fname,
      fontStyle: this.fstyle,
      fontDisplay: 'swap',
      fontWeight: this.fweight,
      src: `
              local(${this.fname}),
              url(${this.furl}) format('woff2')
          `,
      unicodeRange:
        'U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF',
    };
  }
}
const ysDisplay500 = new Font(
  'YS Display',
  'normal',
  500,
  './YSDisplay/YSDisplay-Medium.woff2'
);

const ysText500 = new Font(
  'YS Text',
  'normal',
  500,
  './YSText/YSText-Medium.woff2'
);

const ysDisplay400 = new Font(
  'YS Display',
  'normal',
  400,
  './YSDisplay/YSDisplay-Regular.woff2'
);

const ysText400 = new Font(
  'YS Text',
  'normal',
  400,
  './YSText/YSText-Regular.woff2'
);

export { ysDisplay500, ysText500, ysDisplay400, ysText400 };
