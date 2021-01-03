import React from 'react';
import { Card } from 'antd';
import styled from 'styled-components';

interface IProps {
  title: string;
  description: string;
  image: string;
}

const { Meta } = Card;

const StyledCard = styled(Card)`
  width: 300px;
  height: 100%;
  padding: 8px 9;
`;

const AnimeCard = (props: IProps) => {
  const image = () => {
    return <img alt='example' src={props.image} />;
  };

  return (
    <StyledCard cover={image}>
      <Meta title={props.title} description={props.description} />
    </StyledCard>
  );
};

export default AnimeCard;
