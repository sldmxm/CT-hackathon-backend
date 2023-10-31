import { Typography } from '@mui/material';
import React from 'react';

export function Text({ children }: { children: React.ReactNode }) {
  return (
    <Typography
      sx={{
        fontFamily: 'YS Text',
        fontSize: '16px',
        lineHeight: '20px',
      }}
    >
      {children}
    </Typography>
  );
}
