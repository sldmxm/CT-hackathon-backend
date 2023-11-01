import { Card, ThemeProvider, createTheme } from '@mui/material';

import React from 'react';

import styles from './CustomCard.module.css';

const theme = createTheme({
  components: {
    MuiCard: {
      styleOverrides: {
        root: {
          background: 'var(--interface-main-color-white, #FFF)',
          borderRadius: '20px',
          boxShadow:
            '0px 4px 6px 0px rgba(176, 190, 197, 0.15), 0px 8px 24px 0px rgba(176, 190, 197, 0.15)',
        },
      },
    },
    MuiCardMedia: {
      styleOverrides: {
        root: {
          width: 40,
        },
      },
    },
  },
});

export function CustomCard({
  children,
}: {
  children: React.ReactNode;
}): JSX.Element {
  return (
    <ThemeProvider theme={theme}>
      <Card className={styles.Card}>{children}</Card>
    </ThemeProvider>
  );
}
