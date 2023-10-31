import { createTheme } from '@mui/material';

import {
  ysDisplay500,
  ysText500,
  ysDisplay400,
  ysText400,
} from './assets/fonts';

export const theme = createTheme({
  typography: {
    fontFamily: [
      ysText400.fname,
      'Arial',
      'Helvetica',
      'Arial Unicode MS',
      'sans-serif',
    ].join(','),
    fontSize: 16,
    h3: {
      fontFamily: ysDisplay500.fname,
      fontStyle: 'normal',
      fontWeight: ysDisplay500.fweight,
    },
    h2: {
      fontFamily: ysDisplay500.fname,
      fontStyle: 'normal',
      fontWeight: ysDisplay500.fweight,
    },
  },
  components: {
    MuiCssBaseline: {
      styleOverrides: {
        '@global': {
          '@font-face': [
            ysDisplay500.getFontConfig(),
            ysText500.getFontConfig(),
            ysDisplay400.getFontConfig(),
            ysText400.getFontConfig(),
          ],
        },
      },
    },
  },
});
