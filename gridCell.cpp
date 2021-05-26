#include "gridCell.h"

namespace slam {

GridCell::GridCell() : logOddsValue(0.0f)
{

}

GridCell::~GridCell()
{

}

void GridCell::setLogOddsValue( float logOddsValue )
{
	this->logOddsValue = logOddsValue;
}

float GridCell::getLogOddsValue() const
{
	return logOddsValue;
}

bool GridCell::isOccupied() const
{
	return ( logOddsValue > 0.0f );
}

bool GridCell::isFree() const
{
	return ( logOddsValue < 0.0f );
}

bool GridCell::isUnknow() const
{
	return ( logOddsValue == 0.0f );
}

void GridCell::resetGridCell()
{
	logOddsValue = 0.0f;
}

}
