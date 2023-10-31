import { Box, Typography } from '@mui/material';
import React from 'react';

export function CardContentWrapper({
  children,
  title,
}: {
  children: React.ReactNode;
  title: string;
}) {
  return (
    <Box
      sx={{
        display: 'flex',
        maxWidth: '708px',
        flexDirection: 'column',
        alignItems: 'flex-start',
        gap: '12px',
        flexShrink: 0,
      }}
    >
      <Typography
        variant='h3'
        sx={{
          color: '#797980',
          fontSize: '24px',
          lineHeight: '24px',
        }}
      >
        {title}
      </Typography>
      {children}
    </Box>
  );
}
