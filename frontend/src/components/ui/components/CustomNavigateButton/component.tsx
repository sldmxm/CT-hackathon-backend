import { Tabs, Tab, createTheme, ThemeProvider } from '@mui/material';
import React from 'react';

const theme = createTheme({
  components: {
    MuiTabs: {
      styleOverrides: {
        root: {
          minHeight: 32,
          marginBottom: 24,
        },
        scroller: {
          height: 32,
        },
        indicator: {
          height: 1,
          backgroundColor: 'var(--primary-black-500, #797980)',
        },
        flexContainer: {
          gap: 20,
        },
      },
    },
    MuiTab: {
      styleOverrides: {
        root: {
          padding: '0',

          fontfamily: 'YS Display',
          fontSize: 24,
          fontStyle: 'normal',
          fontWeight: 400,
          textAlign: 'center',
          textTransform: 'none',
          minHeight: 32,
          '&.Mui-selected': {
            color: 'black',
          },
        },
      },
    },
  },
});

interface CustomNavigateButtonProps {
  value: number;
  onChange: (_event: React.SyntheticEvent, newValue: number) => void;
  labels: string[];
}

export function CustomNavigateButton(props: CustomNavigateButtonProps) {
  const { value, onChange, labels } = props;
  return (
    <ThemeProvider theme={theme}>
      <Tabs value={value} onChange={onChange} aria-label='basic tabs example'>
        {labels.map((label, index) => (
          <Tab key={index} label={label} />
        ))}
      </Tabs>
    </ThemeProvider>
  );
}
