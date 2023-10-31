import { ThemeProvider } from '@emotion/react';
import { createTheme, Card } from '@mui/material';
import cn from 'classnames';

import styles from './candidate.module.css';

const theme = createTheme({
  components: {
    MuiCard: {
      styleOverrides: {
        root: {
          display: 'flex',
          boxSizing: 'border-box',
          flexDirection: 'column',
          alignItems: 'flex-start',
          padding: '16px 20px 20px 20px',
          gap: 12,
          borderRadius: 20,
          boxShadow:
            '0px 4px 6px 0px rgba(176, 190, 197, 0.15), 0px 8px 24px 0px rgba(176, 190, 197, 0.15)',
        },
      },
    },
  },
});

export function CardProvider({
  children,
  isActive,
}: {
  children: React.ReactNode;
  isActive?: boolean;
}) {
  return (
    <ThemeProvider theme={theme}>
      <Card
        className={cn(styles.candidate, {
          [styles.active]: isActive,
        })}
      >
        {children}
      </Card>
    </ThemeProvider>
  );
}
