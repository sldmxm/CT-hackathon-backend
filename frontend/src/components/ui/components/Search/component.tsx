import { TextField, InputAdornment } from '@mui/material';

import styles from './Search.module.css';

import { SearchIcon } from '../../icons/SearchIcon';

export function Search() {
  return (
    <form className={styles.form}>
      <TextField
        className={styles.inputFormControl}
        placeholder='Поиск по вакансиям'
        variant='outlined'
        InputProps={{
          style: { padding: 0 },
          classes: {
            root: styles.myRootClass,
          },
          startAdornment: (
            <InputAdornment position='start' className={styles.inputImg}>
              <SearchIcon />
            </InputAdornment>
          ),
        }}
        inputProps={{
          style: { padding: 0, width: '100%', height: '40px' },
        }}
        InputLabelProps={{
          shrink: true,
        }}
        FormHelperTextProps={{
          style: { padding: 0 },
        }}
      />
    </form>
  );
}
