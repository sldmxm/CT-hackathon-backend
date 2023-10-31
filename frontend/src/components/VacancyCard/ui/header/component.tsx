import { CardHeader, Avatar, Typography, IconButton } from '@mui/material';
import cn from 'classnames';

import { ArrowIcon } from '../../../ui/icons';
import styles from '../Ui.module.css';

interface VacancyCardHeaderProps {
  image: string;
  title: string;
  expanded: boolean;
  handleExpandClick: () => void;
}

export function VacancyCardHeader({
  image,
  title,
  handleExpandClick,
  expanded,
}: VacancyCardHeaderProps) {
  return (
    <CardHeader
      sx={{
        padding: 0,
        margin: 0,
        maxWidth: '400px',
      }}
      avatar={<Avatar src={image} />}
      title={
        <Typography
          variant='h2'
          component='h2'
          children={title}
          sx={{
            fontSize: '24px',
            lineHeight: '32px',
            whiteSpace: 'nowrap',
          }}
        />
      }
      action={
        <IconButton
          disableRipple
          onClick={handleExpandClick}
          className={cn(styles.rotateButton, {
            [styles.expanded]: expanded,
          })}
        >
          <ArrowIcon />
        </IconButton>
      }
    />
  );
}
