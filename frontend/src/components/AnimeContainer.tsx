import React from 'react';
import { Row, Col, Divider, Input } from 'antd';
import AnimeCard from './AnimeCard';
import styled from 'styled-components';

const StyledContainer = styled.div`
  padding: 12em;
`;

const AnimeContainer = () => {
  const { Search } = Input;
  const onSearch = (value: any) => console.log(value);

  return (
    <StyledContainer>
      <Search placeholder='input search text' onSearch={onSearch} enterButton />

      <Divider orientation='left'>Responsive</Divider>
      <Row gutter={{ xs: 8, sm: 16, md: 24, lg: 32 }}>
        <Col className='gutter-row' span={6}>
          <AnimeCard
            title='Anime Title'
            description='Anime description'
            image='https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png'
          />
        </Col>
        <Col className='gutter-row' span={6}>
          <AnimeCard
            title='Anime Title'
            description='Anime description'
            image='https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png'
          />
        </Col>
        <Col className='gutter-row' span={6}>
          <AnimeCard
            title='Anime Title'
            description='Anime description'
            image='https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png'
          />
        </Col>
        <Col className='gutter-row' span={6}>
          <AnimeCard
            title='Anime Title'
            description='Anime description'
            image='https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png'
          />
        </Col>
      </Row>
    </StyledContainer>
  );
};

export default AnimeContainer;
