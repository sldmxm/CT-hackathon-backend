import { CardMedia, Typography } from '@mui/material';
import LinearProgress from '@mui/material/LinearProgress';
import { DataGrid, GridColDef, GridRenderCellParams } from '@mui/x-data-grid';

import { useEffect, useState } from 'react';

import styles from './candidate-list.module.css';

import { Candidate } from '../../interfaces/candidate.interface';
import { selectCandidatesModule } from '../../redux-store/candidates/selector';
import { fetchCandidates } from '../../redux-store/candidates/thunk/fetchCandidates';
import { useAppDispatch, useAppSelector } from '../../redux-store/store';

import { Tag } from '../ui/components/Tag/component';
import { RelocateIcon } from '../ui/icons/RelocateIcon';

type TRow = {
  id: number;
  person: Candidate;
  office_format: string[];
  current_location: string[];
  work_format: string[];
  work_experience: string;
  status: string;
  hard_skills: string[];
};

const columns: GridColDef[] = [
  {
    field: 'id',
    renderHeader: () => <Typography variant='body1'>№</Typography>,
    width: 48,
    hideSortIcons: true,
  },
  {
    field: 'person',
    renderHeader: () => <Typography variant='body1'>Кандидат</Typography>,
    headerName: 'Кандидат',
    width: 244,
    renderCell: (params: GridRenderCellParams<Candidate>) => (
      <a href='#' className={styles.person}>
        <div className={styles['photo-wrapper']}>
          <CardMedia
            component='img'
            src={params.value.image ? params.value.image : 'null'}
            alt={`${params.value.first_name} ${params.value.last_name}`}
            title={`${params.value.first_name} ${params.value.last_name}`}
            height='36'
            width='36'
            image={params.value.image}
          />
        </div>
        <Typography variant='body2'>
          {params.value.first_name} {params.value.last_name}
        </Typography>
      </a>
    ),
    hideSortIcons: true,
  },
  {
    field: 'office_format',
    renderHeader: () => <Typography variant='body1'>Формат</Typography>,
    width: 100,
    hideSortIcons: true,
  },
  {
    field: 'current_location',
    renderHeader: () => <Typography variant='body1'>Регион</Typography>,
    width: 120,
    renderCell: (params: GridRenderCellParams<string[]>) => {
      const currentLocation: string = params.value[0];

      return (
        <div
          className={styles.location}
          title={
            params.value.length > 1 ? 'Готов к переезду' : 'Не готов к переезду'
          }
        >
          <Typography variant='body2' className={styles['location__current']}>
            {currentLocation}
          </Typography>
          {params.value.length > 1 && <RelocateIcon />}
        </div>
      );
    },
    hideSortIcons: true,
  },
  {
    field: 'work_format',
    renderHeader: () => <Typography variant='body1'>График</Typography>,
    width: 120,
    hideSortIcons: true,
  },
  {
    field: 'work_experience',
    renderHeader: () => <Typography variant='body1'>Опыт</Typography>,
    width: 80,
    hideSortIcons: true,
  },
  {
    field: 'status',
    renderHeader: () => <Typography variant='body1'>Статус</Typography>,
    width: 140,
    renderCell: (params: GridRenderCellParams<string[]>) => {
      const statuses = [
        'Пассивно ищу работу',
        'Активно ищу работу',
        'Не ищу работу',
        'Открыт для предложений',
        'Ищу дополнительную работу',
      ];
      const colors = ['#FFE1BD', '#C2E5CE', '#FFDDE5', '#CCC2ED', '#FFF9D3'];
      let color;

      switch (params.value) {
        case statuses[0]:
          color = colors[0];
          break;

        case statuses[1]:
          color = colors[1];
          break;

        case statuses[2]:
          color = colors[2];
          break;

        case statuses[3]:
          color = colors[3];
          break;

        case statuses[4]:
          color = colors[4];
          break;
      }

      return (
        <div
          className={styles.status}
          style={{
            backgroundColor: color,
          }}
          title={params.value}
        >
          <Typography variant='body2' className={styles['status__text']}>
            {params.value}
          </Typography>
        </div>
      );
    },
    hideSortIcons: true,
  },
  {
    field: 'hard_skills',
    renderHeader: () => <Typography variant='body1'>Навыки</Typography>,
    width: 344,
    renderCell: (params: GridRenderCellParams<string[]>) => (
      <div className={styles.tags}>
        {params.value.map((item: string, i: number) => (
          <Tag text={item} key={i} />
        ))}
      </div>
    ),
    hideSortIcons: true,
  },
];

export function CandidateList(): JSX.Element {
  const dispatch = useAppDispatch();
  const candidates = useAppSelector(selectCandidatesModule);
  const [rows, setRows] = useState([] as TRow[]);

  const getRows = (persons: Candidate[]) => {
    const rows = [...persons].map((person, i) => {
      return {
        id: i + 1,
        person,
        office_format: person.office_format.map((format) => format.name),
        current_location: [
          person.current_location,
          ...person.location_to_relocate.map((location) => location.name),
        ],
        work_format: person.work_format.map((format) => format.name),
        work_experience: person.work_experience,
        status: person.status,
        hard_skills: person.hard_skills.map((skill) => skill.name),
      };
    });

    return rows;
  };

  useEffect(() => {
    if (candidates.length == 0) {
      dispatch(fetchCandidates());
    }

    setRows(getRows(candidates));
  }, [candidates, dispatch]);

  return (
    <div className={styles.candidates} style={{ width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        autoHeight
        disableColumnMenu
        slots={{
          loadingOverlay: LinearProgress,
        }}
        loading={rows.length === 0}
        sx={{ '--DataGrid-overlayHeight': '500px', border: 'none' }}
        initialState={{
          pagination: {
            paginationModel: { page: 0, pageSize: 10 },
          },
        }}
        pageSizeOptions={[5, 10]}
        checkboxSelection
      />
    </div>
  );
}
