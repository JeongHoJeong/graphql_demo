import React from 'react'
import { graphql, QueryRenderer } from 'react-relay'

import environment from '../relay'

import { Table } from 'antd'

export class UserList extends React.Component {
  constructor(props) {
    super(props)

    this.state = {}

    this.renderUsers = this.renderUsers.bind(this)
  }

  getColumns() {
    return [
      {
        title: 'ID',
        key: 'id',
        dataIndex: 'id',
      },
      {
        title: '이름',
        key: 'name',
        dataIndex: 'name',
      },
      {
        title: '생일',
        key: 'birthdate',
        dataIndex: 'birthdate',
      },
    ]
  }

  renderUsers({error, props}) {
    if (error) {
      return <div>Error occured loading user list.</div>
    }

    const loading = Boolean(!props)

    return (
      <Table
        rowKey='id'
        dataSource={(props && props.users) || []}
        loading={loading}
        columns={this.getColumns()}
      />
    )
  }

  render() {
    return (
      <QueryRenderer
        environment={environment}
        query={graphql`
        query UserListQuery {
          users {
            id,
            name,
            birthdate
          }
        }
        `}
        variables={{}}
        render={this.renderUsers}
      />
    )
  }
}
